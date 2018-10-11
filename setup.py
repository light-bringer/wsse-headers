import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = ""

packages = ['WsseHeaders']

requires = [
    'pycrypto>=2.6.1',
    'pytz>=2018.5'
]

setuptools.setup(
    name="WsseHeaders",
    version="0.0.1c",
    author="Debapriya Das",
    author_email="yodebu@gmail.com",
    description="A package to generate WSSE Headers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/light-bringer/wsse-headers",
    # packages=setuptools.find_packages(),
    packages = packages,
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)