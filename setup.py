import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = ""

setuptools.setup(
    name="wsse_headers",
    version="0.0.1",
    author="Debapriya Das",
    author_email="yodebu@gmail.com",
    description="A package to generate WSSE Headers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/light-bringer/wsse-headers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)