from setuptools import find_packages, setup
setup(
    name='GeoLibrary',
    packages=find_packages(),
    version='0.1.0',
    description='A Geocoding Library',
    author='Kelly Zhang',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)