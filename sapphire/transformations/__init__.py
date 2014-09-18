"""Transformation modules

Easy transformations between different systems.

:mod:`~sapphire.angles`
    conversion between different angle notations

:mod:`~sapphire.axes`
    rotation matrices and conversion between coordinate systems

:mod:`~sapphire.base`
    conversion betweeen decimal and sexagesimal

:mod:`~sapphire.clock`
    conversion between different time keeping systems

:mod:`~sapphire.geographic`
    geographic coordinate transformations (e.g. WGS84 to ENU)

"""
from . import angles
from . import axes
from . import base
from . import clock
from . import geographic


__all__ = ['angles',
           'axes',
           'base',
           'geographic',
           'clock',
           'geographic']