"""\
The setup uses pbr for package management.
See setup.cfg for real configuration
"""
import setuptools

setuptools.setup(setup_requires=["pbr", "setuptools"], pbr=True)
