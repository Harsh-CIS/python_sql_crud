"""Account Details."""
from time import sleep
from user.user_info import User
from common.validation import confirmation


class Account(User):
    """Account Info."""

    def __init__(self):
        """Init method."""
        super().__init__()
        # super().user_info()
        # super().personel()
        self.transaction()

    def transaction(self):
        """For Transaction."""
        self.balance_list = []
        self.transact = input("Do you want to perform transactions(y/n). ")
        while self.transact == 'y':
            self.value = {'confirm': 'transact'}
            self.balance = confirmation(self.transact, self.balance, **self.value)
            print("Current Balance", self.balance)
            self.balance_list.append(self.balance)
            self.transact = input("Do you want to perform transactions(yes/n). ")
        print("Please wait while we generate your statement.....")
        sleep(1.5)

    def statement(self):
        """For printing the statement."""
        line1 = "Name:-  " + self.first_name + ' ' + self.last_name
        line2 = "Account no :-  " + self.account_number
        line3 = "Contact no :-  " + self.phone_number
        line4 = "---------------------------------------------------------" + "\n"
        # self.line4 = "Marital Status :-  " + married
        file = open("statement.txt", "+w")
        file.writelines([line1 + '\n', line2 + '\n', line3 + '\n', line4 + '\n'])
        # import pdb;pdb.set_trace()
        if len(self.balance_list) > 0:
            if len(self.balance_list) == 1:
                line5 = ".................................................................{} \n".format(self.balance_list[0])
                file.write(line5 + "\n")
            else:
                for amount in range(0, len(self.balance_list) - 1):
                    line6 = "..........................................................{} \n".format(self.balance_list[amount])
                    file.write(line6 + '\n')
                line7 = "_______________________________________________________________________" + "\n"
                line8 = "Final Amount.................................................{}".format(self.balance_list[len(self.balance_list) - 1])
                file.writelines([line7 + '\n', line8 + '\n'])
        else:
            file.write("------------There were no Transactions---------------")
        file.close()
