from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements()->List[str]:
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        print("hi")
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="Network Security",
    Version="1.0",
    author='Prash',
    author_email='prasanthdraksharapu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)