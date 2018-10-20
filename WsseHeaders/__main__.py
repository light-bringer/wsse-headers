import sys
import WsseHeaders


def main():
    if (len(sys.argv) < 3):
        print("Usage: <USERNAME> <ORGANIZATION> <TOKEN>")
    else:
        a = WsseHeaders.WsseToken(sys.argv[0], sys.argv[1], sys.argv[2])
        headers = a.generateHeaders()
        return headers


if __name__ == "__main__":
    main()