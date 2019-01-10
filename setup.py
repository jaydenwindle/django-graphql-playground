import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='graphql_playground',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Apollo GraphQL Playground as a Django view',
    long_description=README,
    url='https://jaydenwindle.com/',
    author='Jayden Windle',
    author_email='jaydenwindle@gmail.com',
)