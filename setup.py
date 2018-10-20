import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))
long_description = ""
try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = """
    WsseHeaders: WSSE for Python™
    ==========================


        WsseHeaders is the only WSSE Token generation library for Python, safe for human
        consumption.


        ``` {.sourceCode .python}
        >>> import WsseHeaders
        >>> r = WsseHeaders.WsseToken(username="yodebu", orgName="yodebu", token="base64tokenstring")
        >>> r.generateHeaders()
        UsernameToken Username="yodebu", PasswordDigest="EU4mrjk9tD3AVl3N1oJ6Yc+PA4k=", Nonce="e52165a00ae24d62bd44adb96f7c95dd", Created="2018-10-16T19:51:43+00:00", Organization="EXAMPLE_ORG"
        ```

        optional parameter: ``` pad ``` which is defaulted to ``` False``` and takes only Boolean values.

        ``` {.sourceCode .python}
        >>> import WsseHeaders
        >>> r = WsseHeaders.WsseToken(username="yodebu", orgName="yodebu", token="base64tokenstring", pad=True)
        >>> r.generateHeaders()
        UsernameToken Username="yodebu", PasswordDigest="EU4mrjk9tD3AVl3N1oJ6Yc+PA4k=", Nonce="e52165a00ae24d62bd44adb96f7c95dd", Created="2018-10-16T19:51:43+00:00", Organization="EXAMPLE_ORG"
        ```


        WsseHeaders officially supports Python 3.0 and above.

        Installation
        ------------

        To install WsseHeaders, simply use [pipenv](http://pipenv.org/) (or pip, of
        course):

        ``` {.sourceCode .bash}
        $ pipenv install WsseHeaders
        ✨🍰✨
        ```


        Documentation
        -------------

        Fantastic documentation to be available shortly at
        <http://docs.python.org/>, for a limited time only.

        How to Contribute
        -----------------

        1.  Check for open issues or open a fresh issue to start a discussion
            around a feature idea or a bug. 
        2.  Fork [the repository](https://github.com/light-bringer/wsse-headers) on
            GitHub to start making your changes to the **master** branch (or
            branch off of it).
        3.  Write a test which shows that the bug was fixed or that the feature
            works as expected.
        4.  Send a pull request and bug the maintainer until it gets merged and
            published. :) Make sure to add yourself to
            [AUTHORS](https://github.com/light-bringer/wsse-headers/blob/master/AUTHORS.rst).
    """

packages = ['WsseHeaders']

requires = [
    'pycrypto>=2.6.1',
    'pytz>=2018.5'
]

setuptools.setup(
    name="WsseHeaders",
    version="0.0.7c",
    author="Debapriya Das",
    author_email="yodebu@gmail.com",
    description="A package to generate WSSE Headers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/light-bringer/wsse-headers",
    # packages=setuptools.find_packages(),
    keywords='WSSE Headers generation',
    packages = packages,
    python_requires=">=3.0, <4",
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)