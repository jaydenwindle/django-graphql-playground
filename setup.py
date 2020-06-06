import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-graphql-playground',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Apollo GraphQL Playground as a Django view',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://jaydenwindle.com/',
    author='Jayden Windle',
    author_email='jaydenwindle@gmail.com',
)
