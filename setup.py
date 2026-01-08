from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='mlproject_2026',
    version='0.0.1',
    author='damintha deshan wijekoon',
    author_email='daminthadeshan01.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )

