from setuptools import find_packages,setup
from typing import List

LINKING_CONSTANT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if LINKING_CONSTANT in requirements:
            requirements.remove(LINKING_CONSTANT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Suryash',
author_email='suryash.c@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 

)