import os
import os.path
from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def find_requires():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open('{0}/requirements.txt'.format(dir_path), 'r') as reqs:
        requirements = reqs.readlines()
    return requirements


if __name__ == "__main__":
    setup(
        name="advanced-argparse",
        version="0.1.0",
        author="Alex Gorodnitskiy",
        author_email="alexander.gorodnitskiy@phystech.edu",
        description='Advanced parser based on argparse and YAML config',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=find_requires(),
        include_package_data=True
    )
