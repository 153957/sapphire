from __future__ import division

import tables
import time

from sapphire.analysis import process_events


N = None


def show_processing_time(events, dt, limit):
    if limit:
        guess_dt = len(events) / limit * dt
    else:
        guess_dt = dt
        limit = len(events)
    print "Processing %d events: %.2f s" % (limit, dt)
    print "Estimate for total processing time: %.2f h" % (guess_dt / 3600)


if __name__ == '__main__':
    try:
        data
    except NameError:
        data = tables.openFile('kascade.h5', 'a')

    group = data.root.hisparc.cluster_kascade.station_601

    if '_t_events' in group:
        group._t_events.remove()

    indexes = data.root.kascade.c_index[:,1]
    cls = process_events.ProcessIndexedEvents(data, group, indexes,
                                              overwrite=True)

    t0 = time.time()
    cls.process_and_store_results()
    dt = time.time() - t0
    show_processing_time(data.root.hisparc.cluster_kascade.station_601.events,
                         dt, N)

    event = group.events[indexes[0]]
    print [event['t%d' % u] for u in 1, 2, 3, 4]
