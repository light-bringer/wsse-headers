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

        Initialize the WsseHeader module

        ``` {.sourceCode .python}
        >>> import WsseHeaders
        >>> WsseTokenObject = WsseHeaders.WsseToken(username="yodebu", orgName="yodebuOrg", token="base64tokenstring")
        ```

        Generate the Header String as required : 

        ``` {.sourceCode .python}
        >>> WsseTokenObject.generateHeaderString()
        'UsernameToken Username="yodebu", PasswordDigest="SXoO32oqIKFOl63mvsMoW+HPcHo=", Nonce="/lruYfbC12FfjiqFLgJxVw==", Created="2018-11-11T10:50:49+00:00", Organization="yodebuOrg"'
        ```
        Get the Authentication Headers as Dictionary which can be easily converted to JSON: 

        ``` {.sourceCode .python}
        >>> WsseTokenObject.generateHeader()
        {
            'Authorization': 'WSSE profile="UsernameToken"', 
            'X-WSSE': 'UsernameToken Username="yodebu", PasswordDigest="SXoO32oqIKFOl63mvsMoW+HPcHo=", Nonce="/lruYfbC12FfjiqFLgJxVw==", Created="2018-11-11T10:50:49+00:00", Organization="yodebuOrg"', 
            'Accept': 'Application/json'
        }
        ```

        WsseHeaders officially supports Python 3.0 and above. Python 2.7 support coming soon.

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
    'pycryptodome>=3.7.0',
    'pytz>=2018.5'
]

setuptools.setup(
    name="WsseHeaders",
    version="0.0.16",
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