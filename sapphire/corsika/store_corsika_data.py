#!/usr/bin/env python

""" Store CORSIKA simulation data in HDF5 file

    This module reads the CORSIKA binary ground particles file and stores
    each particle individually in a HDF5 file, using PyTables.  This file
    can then be used as input for the detector simulation.

"""

import tables

from sapphire import corsika

SEED_NUMBERS = '131245_34234536'

SOURCE_FILE = '/Users/niekschultheiss/corsika_data/' + SEED_NUMBERS + '/DAT000000'
DEST_FILE = '/Users/niekschultheiss/corsika_data/' + SEED_NUMBERS + '/data.h5'


class GroundParticles(tables.IsDescription):
    """Store information about shower particles reaching ground level"""

    particle_id = tables.UInt16Col(pos=0)
    r = tables.Float32Col(pos=1)
    phi = tables.Float32Col(pos=2)
    x = tables.Float32Col(pos=3)
    y = tables.Float32Col(pos=4)
    t = tables.Float32Col(pos=5)
    p_x = tables.Float32Col(pos=6)
    p_y = tables.Float32Col(pos=7)
    p_z = tables.Float32Col(pos=8)
    hadron_generation = tables.UInt8Col(pos=9)
    observation_level = tables.UInt8Col(pos=10)


def save_particle(row, p):
    """Write the information of a particle into a row"""

    (p_x, p_y, p_z, x, y, t, id, r, hadron_generation, observation_level,
     phi) = p

    row['particle_id'] = id
    row['r'] = r
    row['phi'] = phi
    row['x'] = x
    row['y'] = y
    row['t'] = t
    row['p_x'] = p_x
    row['p_y'] = p_y
    row['p_z'] = p_z
    row['hadron_generation'] = hadron_generation
    row['observation_level'] = observation_level
    row.append()


def store_corsika_data(source, destination, table_name='groundparticles'):

    """Store particles from a CORSIKA simulation in a HDF5 file

    :param source: CorsikaFile instance of the source DAT file
    :param destination: PyTables file instance of the destination file

    """

    print "Storing CORSIKA data (%s) in %s" % (source._filename,
                                               destination.filename)
    source.check()

    for event in source.get_events():
        n_particles = event.get_end().n_particles_levels
        try:
            table = destination.createTable('/', table_name, GroundParticles,
                                            'All groundparticles',
                                            expectedrows=n_particles)
        except tables.NodeError:
            print '%s already exists, doing nothing' % table_name
            return
        particle_row = table.row
        for particle in event.get_particles():
            save_particle(particle_row, particle)

    table.flush()

    run_header = source.get_header()
    run_end = source.get_end()
    for event in source.get_events():
        event_header = event.get_header()
        event_end = event.get_end()

    table._v_attrs.run_header = run_header
    table._v_attrs.run_end = run_end
    table._v_attrs.event_header = event_header
    table._v_attrs.event_end = event_end

    table.flush()


if __name__ == '__main__':
    # Source
    corsika_data = corsika.CorsikaFile(SOURCE_FILE)

    # Destination
    hdf_data = tables.openFile(DEST_FILE, 'w')

    store_corsika_data(corsika_data, hdf_data)

    hdf_data.close()
