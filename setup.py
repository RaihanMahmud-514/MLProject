from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ")for req in requirements]

setup(
    name='MLProject',
    version='0.0.1',
    author='Md Raihan Mahmud',
    author_email='raihan.mahmud514@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)