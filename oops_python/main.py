"""Main File."""
from common import compat
from account.account import Account


def main():
    """Main Method."""
    user = Account()
    user.statement()
if __name__ == '__main__':

    main()
