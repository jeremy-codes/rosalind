import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rosalindutils",
    version="1.0.0",
    author="Jeremy Adams",
    author_email="jeremybr.adams@gmail.com",
    description="Common Bioinformatics utilities for Rosalind challenges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremy-codes/rosalind",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
