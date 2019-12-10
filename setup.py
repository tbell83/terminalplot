import setuptools
import codecs
import os

here = os.path.absos.path(os.path.dirname(__file__))

with codecs.open( os.path.join(here, 'terminalplot','version.py'),
                  encoding='utf-8' ) as f:
    exec(f.read())

with codecs.open( os.path.join(here, 'README.rst'),
                  encoding='utf-8' ) as f:
    readme = f.read()

setuptools.setup(
    name='terminalplot',
    version=__version__ + 'dev' + os.getenv('TRAVIS_JOB_NUMBER', ''),
    description='Plot points in terminal',
    long_description=readme,
    url='https://github.com/kressi/terminalplot',
    download_url='https://github.com/kressi/terminalplot/tarball/v'+__version__,
    author='Michael Kressibucher',
    author_email='michael.kressibucher@gmail.com',
    license='GPL',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords=['plot', 'terminal', 'graph', 'console'],
    packages=['terminalplot'],
    zip_safe=True,
    entry_points={
        'console_scripts': ['plot = terminalplot.command:main']
    },
    test_suite='nose.collector',
    tests_require=['nose']
)
