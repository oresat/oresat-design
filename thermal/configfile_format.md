Thermsat Configfiles
====================

The preferred method for creating a thermsat object for simulation is to implement a
python configfile which sets all important satellite properties, and can then be modified
to adjust parameters.

Format
------
The format for a Python configfile is simple:
[Section1]
Property1 = Value1
Property2 = Value2 

[Section2]
Property1 = Value1

etc.

The configparser implemented in the thermsat module looks for these sections:

[thermal] - lists thermal properties and materials. Converted into thermsat properties.
[radiation] - lists radiation properties. Converted into thermsat properties.
[orbit] - lists satellite orbit properties. Sets _sat properties.

Make sure you input sane values! The parser will try to work with whatever you give it;
garbage in, garbage out.


[thermal]
---------
The purpose of the thermal section is to get a total thermal mass for the satellite by adding
the material properties of the different elements together. Add materials in tuple format:

material = mass_in_grams,specific_heat_in_joules_per_gram_kelvin

The class factory will split the string into values and then multiply them together,
then sum over all the materials to get a total thermal mass and total mass.

Optional parameters:
start_temp: in K. Default 273.15.

[radiation]
-----------
The purpose of the radiation section is to get mean absorptivities and emissivities for the
satellite. Similarly to the thermal section, add materials in tuple format:

material = surface_area_in_cm^2,absorptivity,emissivity

The class factory breaks out the string into values and calculates a mean emissivity and
absorptivity. You can calculate solar panel absorptivity as (1-reflectivity)*(1-efficiency).

[orbit]
-------
Orbit sets properties for the wrapped ephem.EarthSatellite, and uses variable names to make
sure properties are assigned correctly. The necessary properties are:

_epoch — Reference epoch
_n — Mean motion, in revolutions per day
_inc — Inclination
_raan — Right Ascension of ascending node
_e — Eccentricity
_ap — Argument of perigee at epoch
_M — Mean anomaly from perigee at epoch
_decay — Orbit decay rate in revolutions per day, per day
_drag — Object drag coefficient in per earth radii
_orbit — Integer orbit number of epoch

As an alternative, you can specify a TLE as a three-line object or tuple:

TLE = line1
    line2
    line3

or

TLE = line1,line2,line3

Missing any of these parameters will throw a value error. You can also specify:

angle_format: 'degrees' or 'radians'. Default is radians.
name: name of the satellite
catalog_number: catalog id of the satellite
time: simulation start time [not currently implemented - defaults to now()]

