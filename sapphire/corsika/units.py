"""Defines units in terms of HiSPARC standard units

You should use the units defined in this file whenever you
have a dimensional quantity in your code.  For example:

Do:

.. code-block:: python

    >>> distance = 1.5 * km

Don't:

.. code-block:: python

    >>> distance = 1.5  # don't forget this is in km!

The conversion factors defined in this file convert your data into
HiSPARC base units, so that all dimensional quantities in the code are
in a single system of units!  You can also use the conversions defined
here to, for example, display data with the unit of your choice.  For
example:

.. code-block:: python

    >>> print("distance = %f mm" %  distance / mm)
    1500000 mm

The base units are:

- meter (meter)
- nanosecond (nanosecond)
- electron Volt (eV)
- positron charge (eplus)
- degree Kelvin (kelvin)
- the amount of substance (mole)
- luminous intensity (candela)
- radian (radian)
- steradian (steradian)

The SI numerical value of the positron charge is defined here,
as it is needed for conversion factor: positron charge = eSI (coulomb)

This is a slightly modified version of the units definitions
written by the Geant4 collaboration.

Authors:

- M Maire
- S Giani
- T Paul (modifications for Auger)
- Arne de Laat <adelaat@nikhef.nl>

"""

# math constants
kPi = 3.1415926535897932384626
kPiOnTwo = 0.5 * kPi
kTwoPi = 2 * kPi
kE = 2.7182818284590452353602
kLn10 = 2.3025850929940456840180
kSqrt2 = 1.4142135623730950488017
kSqrt3 = 1.7320508075688772935274
kSqrt2Pi = 2.5066282746310005024158

# Prefixes
yocto = 1e-24
zepto = 1e-21
atto = 1e-18
femto = 1e-15
pico = 1e-12
nano = 1e-9
micro = 1e-6
milli = 1e-3
centi = 1e-2
deci = 1e-1
deka = 1e1
hecto = 1e2
kilo = 1e3
mega = 1e6
giga = 1e9
tera = 1e12
peta = 1e15
exa = 1e18
zetta = 1e21
yotta = 1e24

# Length [L]
meter = 1.0
meter2 = meter * meter
meter3 = meter * meter * meter

millimeter = milli * meter
millimeter2 = millimeter * millimeter
millimeter3 = millimeter * millimeter * millimeter

centimeter = centi * meter
centimeter2 = centimeter * centimeter
centimeter3 = centimeter * centimeter * centimeter

kilometer = kilo * meter
kilometer2 = kilometer * kilometer
kilometer3 = kilometer * kilometer * kilometer

parsec = 3.0856775807e16 * meter
kiloParsec = kilo * parsec
megaParsec = mega * parsec

micrometer = micro * meter
nanometer = nano * meter
angstrom = 1e-10 * meter
fermi = femto * meter

barn = 1e-28 * meter2
millibarn = milli * barn
microbarn = micro * barn
nanobarn = nano * barn
picobarn = pico * barn

# symbols
mm = millimeter
mm2 = millimeter2
mm3 = millimeter3

cm = centimeter
cm2 = centimeter2
cm3 = centimeter3

m = meter
m2 = meter2
m3 = meter3

km = kilometer
km2 = kilometer2
km3 = kilometer3

# Angle
radian = 1.0
milliradian = milli * radian
degree = (3.14159265358979323846 / 180.0) * radian

steradian = 1.0

# symbols
rad = radian
mrad = milliradian
sr = steradian
deg = degree

# Time [T]
nanosecond = 1.0
nanosecond2 = nanosecond * nanosecond
second = giga * nanosecond
millisecond = milli * second
microsecond = micro * second
picosecond = pico * second
minute = 60 * second
hour = 60 * minute
day = 24 * hour

hertz = 1.0 / second
kilohertz = kilo * hertz
megahertz = mega * hertz

# symbols
ns = nanosecond
s = second
ms = millisecond

# Electric charge [Q]
eplus = 1.0  # positron charge
eSI = 1.602176462e-19  # positron charge in coulomb
coulomb = eplus / eSI  # coulomb = 6.24150e18 * eplus

# Energy [E]
electronvolt = 1.0
megaelectronvolt = mega * electronvolt
kiloelectronvolt = kilo * electronvolt
gigaelectronvolt = giga * electronvolt
teraelectronvolt = tera * electronvolt
petaelectronvolt = peta * electronvolt
exaelectronvolt = exa * electronvolt
zettaelectronvolt = zetta * electronvolt

joule = electronvolt / eSI  # joule = 6.24150e12 * MeV

# symbols
MeV = megaelectronvolt
eV = electronvolt
keV = kiloelectronvolt
GeV = gigaelectronvolt
TeV = teraelectronvolt
PeV = petaelectronvolt
EeV = exaelectronvolt
ZeV = zettaelectronvolt

# Mass [E][T^2][L^-2]
kilogram = joule * second * second / (meter * meter)
gram = milli * kilogram
milligram = milli * gram

# symbols
kg = kilogram
g = gram
mg = milligram

# Power [E][T^-1]
watt = joule / second  # watt = 6.24150e3 * MeV / ns

# Force [E][L^-1]
newton = joule / meter  # newton = 6.24150e9 * MeV / mm

# Pressure [E][L^-3]
pascal = newton / m2  # pascal = 6.24150e3 * MeV / mm3
bar = 100000 * pascal  # bar = 6.24150e8 * MeV / mm3
atmosphere = 101325 * pascal  # atm = 6.32420e8 * MeV / mm3

# symbols
hPa = hecto * pascal

# Electric current [Q][T^-1]
ampere = coulomb / second  # ampere = 6.24150e9 * eplus / ns
milliampere = milli * ampere
microampere = micro * ampere
nanoampere = nano * ampere

# Electric potential [E][Q^-1]
megavolt = megaelectronvolt / eplus
kilovolt = milli * megavolt
volt = micro * megavolt

# Electric resistance [E][T][Q^-2]
ohm = volt / ampere  # ohm = 1.60217e-16 * (MeV / eplus) / (eplus / ns)

# Electric capacitance [Q^2][E^-1]
farad = coulomb / volt  # farad = 6.24150e24 * eplus / megavolt
millifarad = milli * farad
microfarad = micro * farad
nanofarad = nano * farad
picofarad = pico * farad

# Magnetic Flux [T][E][Q^-1]
weber = volt * second  # weber = 1000 * megavolt * ns

# Magnetic Field [T][E][Q^-1][L^-2]
tesla = volt * second / meter2  # tesla = 0.001 * megavolt * ns / mm2

gauss = 1e-4 * tesla
kilogauss = kilo * gauss

# Inductance [T^2][E][Q^-2]
henry = weber / ampere  # henry = 1.60217e-7 * MeV * (ns / eplus) ** 2

# Temperature
kelvin = 1.0

# Amount of substance
mole = 1.0

# Activity [T^-1]
becquerel = 1.0 / second
curie = 3.7e10 * becquerel

# Absorbed dose [L^2][T^-2]
gray = joule / kilogram

# Luminous intensity [I]
candela = 1.0

# Luminous flux [I]
lumen = candela * steradian

# Illuminance [I][L^-2]
lux = lumen / meter2

# Miscellaneous
perCent = 0.01
percent = perCent
perThousand = 0.001
permil = perThousand
perMillion = 0.000001
