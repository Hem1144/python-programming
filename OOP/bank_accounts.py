class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("\nDeposite completed.")
        self.getBalance()

    def vailable_ransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.vailable_ransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.vailable_ransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer complete! ✅\n\n**********")

        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite complete")
        self.getBalance()


class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        #! Here to add a extra functionality, we use super keyword
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.vailable_ransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
