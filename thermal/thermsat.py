import ephem
import datetime
import configparser

#TODO: despite the fact that pyephem does all its math, always, in radians, the EarthSatellite object assumes any angles input are input
#in degrees and automatically down-converts them. This means things like simple assignments between object properties can break, which is insane. 
#figure out the least insane way to mitigate this. Currently implemented: automatically scale all assignments to ephem.Angle object members of _sat

tle = "ISS (ZARYA)", "1 25544U 98067A   15306.33154501  .00009977  00000-0  15416-3 0  9999", "2 25544  51.6441 114.6139 0006754 101.7020 328.7420 15.54757498969534"
paramlist = ['_M', '_epoch', '_raan', '_inc', '_drag', '_decay', '_e', '_ap', '_n', '_orbit']

solar_constant = 1366 #insolation per square meter near the earth (W/m**2)
sigma = 5.67036713E-8 #stefan-boltzman constant for black body radiation (W/(m**2-K**4))

def strftup(s, delim):
    return (float(x.strip()) for x in s.split(delim))

#This is a wrapper for the ephem.EarthSatellite class. It uses a "contain and delegate" strategy
#to get intuitive access to EarthSatellite native properties and methods through normal dot
#accessing. It is subclassed from object so that we can call the default setattr without
#recursion.
class thermsat(object):
    _sat = None
    _time = None
    heat = None
    mass = None
    thermal_mass = None
    mean_absorptivity = None
    mean_emissivity = None

    solar_area = None
    albedo_area = None
    radiating_area = None
    
    power_generation = 3

    thermal_functions = []

    @property
    def temp(self):
        return self.heat/self.thermal_mass

    def radiation_out(self, dt):
        self.heat -= self.radiating_area*self.mean_emissivity*sigma*dt*self.temp**4

    def radiation_in(self, dt):
        self.heat += self.eclipsed*solar_constant*dt*self.solar_area*self.mean_absorptivity

    def power(self, dt):
        self.heat += self.power_generation*dt
    
    def step(self, dt):
        self._time += datetime.timedelta(0, dt)
        self.compute(self._time)
        for f in self.thermal_functions:
           f(dt)

    #if the default getattr can't find the property we're looking for it throws
    #to _sat to look there too
    def __getattr__(self, name):
        return getattr(self._sat, name)

    #there is no default for setattr so we have to tell it to look in the both thermsat and our EarthSatellite instance
    #also checks hasattr to prevent assignment if the variable doesn't already exist
    #this is useful because accidentally creating duplicate names in our wrapper object overwrites default behavior in the sat object 
    #automatically scales up all input angles from radians to degrees, because the ephem.EarthSatellite object will scale them back
    def __setattr__(self, name, value):
        if hasattr(self, name):
                try:
                    if isinstance(getattr(self._sat, name), ephem.Angle):
                        value /= ephem.degree
                    setattr(self._sat, name, value)
                except:
                    object.__setattr__(self, name, value)
        else:
            try:
                raise AttributeError("'%s.%s' object has no attribute '%s'"%(self.__module__, self.__class__.__name__, name))
            except AttributeError as e:
                print(e.traceback, e.args)

    @classmethod
    def fromfile(cls, cfgfile):
        self = cls()

        cfg = configparser.SafeConfigParser()
        cfg.read(cfgfile)

        self._sat = ephem.EarthSatellite()
     
        if not cfg.has_section('orbit'):
            raise ValueError("Missing section 'orbit' in config file.")
        else:
            orbit = cfg['orbit']
            angle_format = orbit.pop('angle_format', 'radians')
            self._sat.name = orbit.pop('name', 'sat')
            self._sat.catalog_number = orbit.pop('catalog_number', None)
            self._time = datetime.datetime.now()
            try:
                t = orbit.pop('tle') 
                t = t.split('\n')
                self._sat = ephem.readtle(*tuple(t))
            except:
                for name in paramlist:
                    try: 
                        attr = float(orbit.pop(name))
                        if isinstance(getattr(self, name), ephem.Angle) and angle_format is 'radians':
                            attr /= ephem.degree
                        setattr(self, name, attr)
                    except:
                        raise ValueError("Orbital specification in config file incomplete.")
            self.compute(self._time)

        if not cfg.has_section('thermal'): 
            raise ValueError("Missing section 'thermal' in config file.")
        else:
            thermal = cfg['thermal']
            self.mass = 0
            self.thermal_mass = 0
            start_temp = float(thermal.pop('start_temp', 273.15))
            for key in thermal:
                val = thermal.pop(key)
                mass, c = strftup(val, ',')
                self.mass += mass
                self.thermal_mass += mass
            self.heat = start_temp*self.thermal_mass
         
        if not cfg.has_section('radiation'):
            raise ValueError("Missing section 'radiation' in config file.")
        else:
            radiation = cfg['radiation']
            total_area = 0
            area_weighted_absorptivity = 0
            area_weighted_emissivity = 0

            for key in radiation:
                val = radiation.pop(key)
                area, absorb, emit = strftup(val, ',')
                total_area += area
                area_weighted_absorptivity += area*absorb
                area_weighted_emissivity += area*emit
            
            self.mean_absorptivity = area_weighted_absorptivity / total_area 
            self.mean_emissivity = area_weighted_emissivity / total_area
            self.radiating_area = total_area / 10000
            self.solar_area = self.radiating_area / 6       #dummy assignment, assuming it's a cube

        self.thermal_functions.append(self.radiation_in)
        self.thermal_functions.append(self.radiation_out)
        self.thermal_functions.append(self.power)

        return self
