'''iPlayer cli Setup
    @author Johnny Lindon Robinson (john@johnlindon.com)
    @version 0.1.0

    https://github.com/JohnLindonRobinson/iplayer-cli

    This module is used for handling the setup of the cli
'''
from setuptools import setup

setup(
    name='iplayercli',
    version='0.1.0',
    description='A command line interface for the BBC iPlayer.',
    author='Johnny Lindon Robinson',
    url='https://github.com/JohnLindonRobinson/iplayer-cli',
    author_email='john@johnlindon.com',
    license='GPLv2.0',
    packages=['iplayercli'],
    package_dir={'iplayercli': 'src/iplayer-cli'},
    install_requires=[
                    'requests',
                    'beautifulsoup4',
                    'argparse',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Power Users',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
    ],
)
