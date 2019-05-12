"""Prepare for Pypi."""

from distutils.core import setup
setup(
    name='pyatag',         # How you named your package folder (MyLib)
    packages=['pyatag'],   # Chose the same as "name"
    version='0.1.4',      # Start with a small number
    # Chose a license: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    description='Python API to connect ATAG One Thermostat',
    author='Mats',                   # Type in your name
    author_email='mats.nelissen@gmail.com',      # Type in your E-Mail
    url='https://github.com/MatsNl/pyatag',
    install_requires=[
        'asyncio',
        'aiohttp',
        'netifaces'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        #    'Intended Audience :: Developers',    # Define developer audience
        #    'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
