from setuptools import setup, find_packages

setup(
    name='DemoPackage',
    url='https://github.com/YeOldProgrammer/DemoPackage',
    author='Tim Olker',
    # Needed to actually package something
    packages=find_packages(exclude=['tests*']),
    # Needed for dependencies
    install_requires=['cookiecutter', 'click'],
    version='0.3',
    description='An example of a python package from pre-existing code',
)