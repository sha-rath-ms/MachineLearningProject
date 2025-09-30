from typing import List

from setuptools import setup, find_packages


HYPHEN_E_DOT = "-e ."
def get_requirements(file_name: str) -> List[str]:
    """
    This function returns required packages to be installed
    :param file_name: Name of the requirement list file
    :return: List of packages needs to be installed
    """

    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement for requirement in requirements if requirement.strip()]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Sharath",
    author_email="sharathsharu9155@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
