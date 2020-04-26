from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(
    name='robotist',
    version='0.0.1',
    description="Neural Style Transfer Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Amr Kayid",
    author_email="amrmkayid@gmail.com",
    url="https://github.com/amrmkayid/robotist",
    packages=find_packages(),
    install_requires=[
        "torch==1.4.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
