from setuptools import setup, find_packages


setup(name='hisparc-sapphire',
      version='0.11.2',
      packages=find_packages(),
      url='http://github.com/hisparc/sapphire/',
      bugtrack_url='http://github.com/HiSPARC/sapphire/issues',
      license='GPLv3',
      author='David Fokkema',
      author_email='davidf@nikhef.nl',
      maintainer='HiSPARC',
      maintainer_email='beheer@hisparc.nl',
      description='A framework for the HiSPARC experiment',
      long_description=open('README.rst').read(),
      keywords=['HiSPARC', 'Nikhef', 'cosmic rays'],
      classifiers=['Intended Audience :: Science/Research',
                   'Intended Audience :: Education',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Education',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      scripts=['sapphire/corsika/generate_corsika_overview',
               'sapphire/corsika/qsub_corsika',
               'sapphire/corsika/qsub_store_corsika_data',
               'sapphire/corsika/store_corsika_data'],
      package_data={'sapphire': ['data/hisparc_stations.json',
                                 'corsika/LICENSE',
                                 'tests/analysis/PE-testdata.h5',
                                 'tests/corsika/test_data/corsika_overview.h5',
                                 'tests/corsika/test_data/1_2/DAT000000',
                                 'tests/corsika/test_data/1_2/corsika.h5',
                                 'tests/simulations/test_data/corsika.h5',
                                 'tests/simulations/test_data/groundparticles_sim.h5']},
      install_requires=['numpy', 'scipy', 'tables>=3.2.0', 'progressbar2',
                        'lazy', 'mock'],
      test_suite="sapphire.tests",)
