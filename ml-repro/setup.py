from setuptools import find_packages, setup

from metadata import __author__, __name__, __version__

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email="this@that.com",
    url="https://github.com/tmthyjames/reproml",
    description="This is a Data Science python project.",
    packages=find_packages(exclude=["tests.*", "tests", "*.tests"]),
    package_data={"": ["meta.json"]},
    python_requires=">=3.7",
    dependency_links=[],
    include_package_data=True,
    entry_points={"console_scripts": ["reproml=reproml.main:main"]},
)
