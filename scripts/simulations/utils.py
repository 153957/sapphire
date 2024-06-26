"""Utility functions"""

import inspect

import matplotlib.pyplot as plt
import numpy as np

__suffix = ''
__prefix = ''


def set_suffix(suffix):
    global __suffix
    __suffix = suffix


def set_prefix(prefix):
    global __prefix
    __prefix = prefix


def whosparent():
    """Return parent function name of caller"""

    return inspect.stack()[2][3]


def savename(suffix=''):
    """Create a name using caller's name"""

    if suffix:
        suffix = '-%s' % suffix
    return f'plots/{__prefix}{whosparent()}{suffix}{__suffix}'


def saveplot(suffix=''):
    """Save a plot using caller's name"""

    if suffix:
        suffix = '-%s' % suffix
    plt.savefig(f'plots/{__prefix}{whosparent()}{suffix}{__suffix}.pdf')


def savedata(data, suffix=''):
    """Save a plot using caller's name"""

    if suffix:
        suffix = '-%s' % suffix
    filename = f'plots/{__prefix}{whosparent()}{suffix}{__suffix}.txt'
    np.savetxt(filename, data)


def title(text):
    plt.title(text + '\n(%s)' % __suffix)


mylog = np.vectorize(lambda x: np.log10(x) if x > 0 else 0)
