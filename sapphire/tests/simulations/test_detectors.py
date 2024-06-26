import os
import random
import unittest

import numpy as np

from numpy.testing import assert_almost_equal

from sapphire.simulations.detector import ErrorlessSimulation, HiSPARCSimulation

self_path = os.path.dirname(__file__)


class HiSPARCSimulationTest(unittest.TestCase):
    def setUp(self):
        self.simulation = HiSPARCSimulation
        random.seed(1)
        np.random.seed(1)

    def test_simulate_detector_offsets(self):
        self.assertEqual(self.simulation.simulate_detector_offsets(1), [4.49943665734718])
        offsets = self.simulation.simulate_detector_offsets(10000)
        assert_almost_equal(np.mean(offsets), 0.0, 1)
        assert_almost_equal(np.std(offsets), 2.77, 2)

    def test_simulate_detector_offset(self):
        self.assertEqual(self.simulation.simulate_detector_offset(), 4.49943665734718)

    def test_simulate_station_offset(self):
        self.assertEqual(self.simulation.simulate_station_offset(), 25.989525818611867)

    def test_simulate_gps_uncertainty(self):
        self.assertEqual(self.simulation.simulate_gps_uncertainty(), 7.3095541364845875)

    def test_simulate_adc_sampling(self):
        self.assertEqual(self.simulation.simulate_adc_sampling(0), 0)
        self.assertEqual(self.simulation.simulate_adc_sampling(0.1), 2.5)
        self.assertEqual(self.simulation.simulate_adc_sampling(1.25), 2.5)
        self.assertEqual(self.simulation.simulate_adc_sampling(2.5), 2.5)
        self.assertEqual(self.simulation.simulate_adc_sampling(4), 5.0)

    def test_simulate_signal_transport_time(self):
        self.assertEqual(list(self.simulation.simulate_signal_transport_time()), [3.6091128409407927])
        self.assertEqual(list(self.simulation.simulate_signal_transport_time(1)), [5.0938877122170032])
        self.assertEqual(
            list(self.simulation.simulate_signal_transport_time(11)),
            [
                2.5509743680305879,
                3.2759504918578886,
                2.9027453686866318,
                2.7722064380611307,
                2.9975103080633256,
                3.3796483500672148,
                3.5099596226498524,
                4.2053418869706736,
                3.6197480580293133,
                4.9220361334622806,
                3.0411502792684506,
            ],
        )

    def test_simulate_detector_mips(self):
        # Test with single angle
        assert_almost_equal(self.simulation.simulate_detector_mips(1, 0.5), 1.1818585)
        assert_almost_equal(self.simulation.simulate_detector_mips(2, 0.2), 1.8313342374)

        # Test with multiple angles
        assert_almost_equal(self.simulation.simulate_detector_mips(2, np.array([0.5, 1])), 2.58167027)
        assert_almost_equal(self.simulation.simulate_detector_mips(1, np.array([0.5, 1])), 2.21526297)

        # Test limiting detector length
        assert_almost_equal(self.simulation.simulate_detector_mips(1, np.radians(90)), 47.6237460)
        assert_almost_equal(
            self.simulation.simulate_detector_mips(2, np.array([np.radians(90), np.radians(87)])),
            74.6668728,
        )

    def test_generate_core_position(self):
        x, y = self.simulation.generate_core_position(500)
        assert_almost_equal(x, 59.85605947801825)
        assert_almost_equal(y, 317.2896993591305)

    def test_generate_azimuth(self):
        self.assertAlmostEqual(self.simulation.generate_azimuth(), -0.521366120872004)

    def test_generate_energy(self):
        self.assertEqual(self.simulation.generate_energy(), 136117213526167.64)
        io = 1e17
        assert_almost_equal(self.simulation.generate_energy(io, io) / io, 1.0)
        self.assertEqual(self.simulation.generate_energy(alpha=-3), 100005719231473.97)


class ErrorlessSimulationTest(HiSPARCSimulationTest):
    def setUp(self):
        self.simulation = ErrorlessSimulation
        random.seed(1)
        np.random.seed(1)

    def test_simulate_detector_offsets(self):
        self.assertEqual(self.simulation.simulate_detector_offsets(1), [0])
        self.assertEqual(self.simulation.simulate_detector_offsets(100), [0] * 100)

    def test_simulate_detector_offset(self):
        self.assertEqual(self.simulation.simulate_detector_offset(), 0)

    def test_simulate_station_offset(self):
        self.assertEqual(self.simulation.simulate_station_offset(), 0)

    def test_simulate_gps_uncertainty(self):
        self.assertEqual(self.simulation.simulate_gps_uncertainty(), 0)

    def test_simulate_adc_sampling(self):
        self.assertEqual(self.simulation.simulate_adc_sampling(0), 0)
        self.assertEqual(self.simulation.simulate_adc_sampling(0.1), 0.1)
        self.assertEqual(self.simulation.simulate_adc_sampling(1.25), 1.25)
        self.assertEqual(self.simulation.simulate_adc_sampling(2.5), 2.5)
        self.assertEqual(self.simulation.simulate_adc_sampling(4), 4.0)

    def test_simulate_signal_transport_time(self):
        self.assertEqual(list(self.simulation.simulate_signal_transport_time()), [0])
        self.assertEqual(list(self.simulation.simulate_signal_transport_time(1)), [0])
        self.assertEqual(list(self.simulation.simulate_signal_transport_time(11)), [0] * 11)

    def test_simulate_detector_mips(self):
        self.assertEqual(self.simulation.simulate_detector_mips(1, 0.5), 1)
        self.assertEqual(self.simulation.simulate_detector_mips(2, 0.2), 2)
