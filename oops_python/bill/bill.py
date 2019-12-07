"""Transaction Page."""


class Transaction:
    """For Transaction."""

    def withdraw(self, balance):
        """To withdraw money."""
        self.balance = balance
        print(self.balance)
        self.withdraw_amount = input(
            "Enter the ammount you want to Withdraw - ")
        while type(self.withdraw_amount) != int:
            try:
                self.withdraw_amount = int(self.withdraw_amount)
            except ValueError:
                print("Only digits allowed!!!")
                self.withdraw_amount = input(
                    'Enter the ammount you want to Withdraw - ')
            while self.withdraw_amount > self.balance:

                print("Entered amount is more than the current balance!!!!.")
                self.withdraw_amount = input(
                    "Enter again the ammount you want to Withdraw - ")
                break

        self.balance -= self.withdraw_amount
        return self.balance

    def deposit(self, balance):
        """To deposit Money."""
        self.balance = balance
        print(self.balance)
        self.deposit_amount = input(
            "Enter the ammount you want to Deposit - ")
        while type(self.deposit_amount) != int:
            try:
                self.deposit_amount = int(self.deposit_amount)
            except ValueError:
                print("Only digits allowed!!!")
                self.deposit_amount = input(
                    'Enter the ammount you want to Deposit - ')

        self.balance += self.deposit_amount
        return self.balance
