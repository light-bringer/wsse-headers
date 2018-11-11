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
