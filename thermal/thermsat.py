import ephem

tle = "ISS (ZARYA)", "1 25544U 98067A   15306.33154501  .00009977  00000-0  15416-3 0  9999", "2 25544  51.6441 114.6139 0006754 101.7020 328.7420 15.54757498969534"

#This is a wrapper for the ephem.EarthSatellite class. It uses a "contain and delegate" strategy
#to get intuitive access to EarthSatellite native properties and methods through normal dot
#accessing. It is subclassed from object so that we can call the default setattr without
#recursion.
class thermsat(object):
    #initialization is done by creating an EarthSatellite object with ephem.readtle
    #then storing it in an internal satellite property
    def __init__(self, TLE):
        super().__setattr__("_sat", ephem.readtle(TLE[0], TLE[1], TLE[2]))
    
    #if the default getattr can't find the property we're looking for it throws
    #to _sat to look there too
    def __getattr__(self, name):
        return getattr(self._sat, name)

    #setattr is less smart than getattr so we have to use exception handling
    #to make sure it looks both locally and in the _sat object
    def __setattr__(self, name, value):
        try: 
            setattr(self._sat, name, value)
        except AttributeError:
            super().__setattr__(name, value)
                                                                                         
    #New properties go here
    heat = None
