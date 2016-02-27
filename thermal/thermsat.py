import ephem

#TODO: despite the fact that pyephem does all its math, always, in radians, the EarthSatellite object assumes any angles input are input
#in degrees and automatically down-converts them. This means things like simple assignments between object properties can break, which is insane. 
#figure out the least insane way to mitigate this. Currently implemented: automatically scale all assignments to ephem.Angle object members of _sat

tle = "ISS (ZARYA)", "1 25544U 98067A   15306.33154501  .00009977  00000-0  15416-3 0  9999", "2 25544  51.6441 114.6139 0006754 101.7020 328.7420 15.54757498969534"
paramlist = ['_M', '_epoch', '_raan', '_inc', '_drag', '_decay', '_e', '_ap', '_n', '_orbit']


#This is a wrapper for the ephem.EarthSatellite class. It uses a "contain and delegate" strategy
#to get intuitive access to EarthSatellite native properties and methods through normal dot
#accessing. It is subclassed from object so that we can call the default setattr without
#recursion.
class thermsat(object):
    _sat = None
    heat = None

    #Initialization step; gotta figure out how to make the class generators vs. init more streamlined
    def __init__(self, insat = None):        
        if insat is not None:
            self._sat = insat
        else: 
            self._sat = ephem.EarthSatellite()


    #if the default getattr can't find the property we're looking for it throws
    #to _sat to look there too
    def __getattr__(self, name):
        return getattr(self._sat, name)

    #there is no default for setattr so we have to tell it to look in the both thermsat and our EarthSatellite instance
    #also checks hasattr to prevent assignment if the variable doesn't already exist
    #this is useful because accidentally creating duplicate names in our wrapper object overwrites default behavior in the sat object 
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


    #this is a constructor that generates an instance of the class from a TLE by calling the ephem.readtle standalone function
    @classmethod
    def fromtle(cls, tle):
        sat = ephem.readtle(*tle)
        return cls(insat = sat)

    #this is a constructor that generates an instance from the orbital elements, plus drag, epoch and orbit number
    @classmethod
    def fromelements(cls, **kwargs):
        instance = ephem.EarthSatellite()
        paramlist = ['_M', '_epoch', '_raan', '_inc', '_drag', '_decay', '_e', '_ap', '_n', '_orbit']
        val = None
        for name in paramlist:
            val = kwargs.pop(name)
            setattr(instance, name, val)
        try:
            instance.catalog_number = kwargs.pop('catalog_number')
            instance.name = kwargs.pop('name')
        except:
            pass
        if len(kwargs):
            raise UserWarning('Unused keyword args during satellite initialization.')
        return cls(insat = instance)


#    @classmethod
#    def fromfile(cls, cfgfile):
#        return cls(sat = cfgfile)
