import setuptools
from eprof.meta import version
import pkgutil
with open("README.md") as fh:
    long_description = fh.read()

packages=setuptools.find_packages()
print ("Found packages:\n",'\n'.join(packages),end='\n\n')
setuptools.setup(
    name="eprof",
    version=version,
    author="Hugo A",
    scripts=['./eprof/bin/eprof' ],
    long_description_content_type='text/markdown',
    long_description=long_description,
    description="Python package to manipulate eprof lib output",
    url="https://github.com/crazyhouse33/kvhf.git",
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent"
    ],
    install_requires=[
   'kvhf>=0',
   'runstats>=1.8.0'
    ],
    python_requires='>=3.3',
)
