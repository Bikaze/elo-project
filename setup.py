"""
The setup.py file is an essential part of  packaging and distributing Python projects.
It contains metadata about the project and instructions on how to install it.
This file is used by tools like setuptools to build and distribute the package.
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""

    requirement_lst:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            # Read all lines from the requirements file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name='elo_project',
    version='0.1.0',
    author='Clement MUGISHA',
    packages=find_packages(),
    install_requires=get_requirements()
)