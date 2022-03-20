#!/usr/bin/env python3
import pathlib
from setuptools import find_packages, setup
import djangoPolyglot

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="django-polyglot-translator",
    version=djangoPolyglot.__version__,
    description="Polyglot integration for Django Web Framework",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/riccardoFasan/django-polyglot",
    project_urls={
        "BugTracker": "https://github.com/riccardoFasan/django-polyglot/issues",
        "Homepage": "https://github.com/riccardoFasan/django-polyglot",
    },
    author="Riccardo Fasan",
    author_email="fasanriccardo21@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["Django>3.1.7", "polyglot-translator>=2.1.3"],
)
