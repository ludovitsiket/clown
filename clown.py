# scanning ftps connectivity
import sys


def check_existence(address):
    return


def try_connect(adress):
    return


def syntax():
    print('python3 clown.py [ftps address]')
    sys.exit()


def main():
    ip = sys.argv[1]
    if True:
        check_existence(ip)
        try_connect(ip)
    else:
        print('No ftps connection for ', ip)
        sys.exit()


if __name__ == '__main__':
    main()
