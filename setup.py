"""Setup script for deft"""
import os
import setuptools

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# List of required dependencies
REQUIRED = ["numpy", "pandas", "scikit-learn"]

# This call to setup() does all the work
setuptools.setup(
    name="deft",
    version="1.0.0",
    description="A set of simple tools to increase data deftness.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tobias-fyi/deft",
    author="Tobias Reaper",
    author_email="tobyreaper@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=REQUIRED,
)
