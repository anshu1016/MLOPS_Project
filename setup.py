from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove the '-e .' entry for editable installs
    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "MLOPS_Project"
PKG_NAME = "PyDB_Connector"
AUTHOR_USER_NAME = "anshu1016"
AUTHOR_EMAIL = "arunshukla98710@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('./requirements_dev.txt')  # Use the correct function to get the requirements
)
