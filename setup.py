import os
from setuptools import setup, find_packages

#from src import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
requirements = []

setup(
    name = "mathchem",
#    version = ".".join(map(str, VERSION)),
    version = "0.1",
    description = "",
    long_description = read('README.rst'),
    url = '',
    license = 'MIT',
    author = 'Alexander Vasilyev',
    author_email = 'hamster3d@gmail.com',
    packages = ['src'],
    packages = find_packages(exclude=['tests']),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,
#    tests_require = ["nose",],
#    test_suite = "nose.collector",
)
