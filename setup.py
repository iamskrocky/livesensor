from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:

    requirements_List : List[str] = []

    return requirements_List







setup(
name = 'sensor',
version = "0.0.1",
author = "prince",
author_email= " iamskrocky@gmail.com",
packages = find_packages(),

install_reuires = get_requirements(),

)