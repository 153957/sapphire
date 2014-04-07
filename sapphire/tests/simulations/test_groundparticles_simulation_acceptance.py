import os
import unittest

import tables

from perform_simulation import (create_tempfile_path, perform_simulation,
                                test_data_path)


class GroundparticlesSimulationAcceptanceTest(unittest.TestCase):

    def test_simulation_output(self):
        output_path = create_tempfile_path()
        perform_simulation(output_path)
        self.validate_results(test_data_path, output_path)
        os.remove(output_path)

    def validate_results(self, expected_path, actual_path):
        expected_file = tables.open_file(expected_path)
        actual_file = tables.open_file(actual_path)
        
        for station_id in range(4):
            events_path = '/cluster_simulations/station_%d/events' % \
                          station_id
            self.validate_table(events_path, expected_file, actual_file)

        self.validate_table('/coincidences/coincidences', expected_file,
                            actual_file)
    def validate_table(self, table, expected_file, actual_file):
        expected_node = expected_file.getNode(table)
        actual_node = actual_file.getNode(table)

        for colname in expected_node.colnames:
            expected_col = expected_node.col(colname)
            actual_col = actual_node.col(colname)
            if expected_col.shape == actual_col.shape:
                self.assertTrue((expected_col == actual_col).all())
            else:
                self.fail("Columns do not have the same length.")


if __name__ == '__main__':
    unittest.main()
