# scanning ftps connectivity
import sys


def check_existence(address):
    print('Checking connnection existence for', address)


def try_connect(address):
    print('Try connect to address', address)


def syntax():
    print('Syntax: python3 clown.py [ftps address]')


def send_mail(sender, receivers):
    print('Sending mail to', receivers)


def conditions_for_email(i):
    # 5 only for testing purposes
    if i > 5:
        send_mail('x', 'y')
        i = 0


def main():
    attempt = 0
    try:
        ip = sys.argv[1]
        check_existence(ip)
        if try_connect(ip) is True:
            print('Connection established')
        else:
            attempt += 1
            print('No ftps connection for ', ip)
            conditions_for_email(attempt)
            sys.exit()
    except IndexError:
        syntax()
        sys.exit()


if __name__ == '__main__':
    main()
