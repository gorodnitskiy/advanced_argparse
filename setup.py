from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


if __name__ == "__main__":
    setup(
        name="advanced-argparse",
        version="0.1.0",
        author="Alex Gorodnitskiy",
        author_email="alexander.gorodnitskiy@phystech.edu",
        description='Advanced parser based on argparse and YAML config',
        url="https://github.com/gorodnitskiy/advanced_parser",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=["PyYAML"],
        setup_requires=['pytest-runner', 'flake8'],
        tests_require=['pytest'],
        include_package_data=True
    )
