from setuptools import find_packages, setup

# Specify the custom path to setup.cfg
setup_cfg_path = 'path/to/setup.cfg'

setup(
    name='diablo-api-rvd',
    version='1.0.0',
    packages=find_packages(),
    description='Unofficial season build calculator for Blizzards Diablo 3',
    author='Robert van Duursen',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
