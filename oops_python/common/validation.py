"""All VAlidaion methods."""
from bill.bill import Transaction


def int_validation(validate, **value):
    """Validation for integer value."""
    while type(validate) != int:
            try:
                if len(validate) == 10 and value['value_type'] == 'phone_number':
                    validate = int(validate)

                elif value['value_type'] == 'validate':
                    pass
                else:
                    raise ValueError
            except ValueError:
                print("Only digits allowed with length 10")
                validate = input('Enter phone number - ')


def confirmation(validate, balance, **value):
    """Confirmation for yes or no."""
    trans = Transaction()

    while type(validate) != bool:
        if validate is 'y':
            validate = True
            if validate and value['confirm'] == 'transact':
                tans_type = input(
                    "Press 'w' for withdraw and 'd' for deposit - ")
                if tans_type == 'w':
                    balance = trans.withdraw(balance)
                elif tans_type == 'd':
                    balance = trans.deposit(balance)
                return balance
            else:
                break

        elif validate is 'n':
            validate = False
        else:
            validate = input("Only y/n -- ")
