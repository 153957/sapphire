import math
import unittest

from sapphire.corsika import units


class CorsikaUnitsTests(unittest.TestCase):
    def test_base_units(self):
        """Verify that the correct units are one"""

        self.assertEqual(units.meter, 1.0)
        self.assertEqual(units.m, units.meter)
        self.assertEqual(units.nanosecond, 1.0)
        self.assertEqual(units.ns, units.nanosecond)
        self.assertEqual(units.electronvolt, 1.0)
        self.assertEqual(units.eV, units.electronvolt)
        self.assertEqual(units.radian, 1.0)
        self.assertEqual(units.rad, units.radian)
        self.assertEqual(units.eplus, 1.0)
        self.assertEqual(units.volt, 1.0)
        self.assertEqual(units.volt, units.electronvolt / units.eplus)

    def test_corsika_units(self):
        """Verify that other units used in CORSIKA are properly converted"""

        self.assertEqual(units.eSI, 1.602176462e-19)
        self.assertEqual(units.gigaelectronvolt, units.giga * units.eV)
        self.assertEqual(units.GeV, units.gigaelectronvolt)
        self.assertEqual(units.centimeter, units.centi * units.m)
        self.assertEqual(units.cm, units.centimeter)
        self.assertEqual(units.cm2, units.cm * units.cm)
        self.assertEqual(units.second, units.giga * units.ns)
        self.assertEqual(units.s, units.second)
        self.assertEqual(units.EeV, units.exa * units.eV)
        self.assertEqual(units.degree, (math.pi / 180.0) * units.rad)
        self.assertEqual(units.joule, units.eV / units.eSI)
        self.assertEqual(units.joule, units.eV / units.eSI)
        self.assertEqual(units.gram, units.peta * units.joule * units.ns**2 / units.m**2)
        self.assertEqual(units.g, units.gram)

        self.assertEqual(units.tesla, units.giga * units.volt * units.ns / units.m**2)

    def test_prefixes(self):
        """Verify the values of the prefixes"""

        self.assertEqual(units.yocto, 1e-24)
        self.assertEqual(units.zepto, 1e-21)
        self.assertEqual(units.atto, 1e-18)
        self.assertEqual(units.femto, 1e-15)
        self.assertEqual(units.pico, 1e-12)
        self.assertEqual(units.nano, 1e-9)
        self.assertEqual(units.micro, 1e-6)
        self.assertEqual(units.milli, 1e-3)
        self.assertEqual(units.centi, 1e-2)
        self.assertEqual(units.deci, 1e-1)

        self.assertEqual(units.deka, 1e1)
        self.assertEqual(units.hecto, 1e2)
        self.assertEqual(units.kilo, 1e3)
        self.assertEqual(units.mega, 1e6)
        self.assertEqual(units.giga, 1e9)
        self.assertEqual(units.tera, 1e12)
        self.assertEqual(units.peta, 1e15)
        self.assertEqual(units.exa, 1e18)
        self.assertEqual(units.zetta, 1e21)
        self.assertEqual(units.yotta, 1e24)
