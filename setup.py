from setuptools import setup, find_packages

__version__ = "0.0.4"
REPO_NAME = "MLOPS_Project"
PKG_NAME = "PyDB_Connector"
AUTHOR_USER_NAME = "anshu1016"
AUTHOR_EMAIL = "arunshukla98710@gmail.com"

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # FIXED
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pymongo",
        "dnspython",
        "pandas",
        "numpy",
        "ensure",
    ],  # ONLY runtime deps, no `-e .` or test tools here
)
