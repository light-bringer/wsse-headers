from .wsseheader import WsseToken
import sys

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import  __author__, __author_email__, __license__
from .__version__ import __copyright__


def main():
    if (len(sys.argv) < 3):
        print("Usage: <USERNAME> <ORGANIZATION> <TOKEN>")
    else:
        a = WsseToken(sys.argv[0], sys.argv[1], sys.argv[2])
        headers = a.generateHeaders()
        return headers


if __name__ == "__main__":
    main()