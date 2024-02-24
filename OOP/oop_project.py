from bank_accounts import *

Hemlal = BankAccount(10000, "Hemlal")
Dulal = BankAccount(90000, "Dulal")

Hemlal.getBalance()
Dulal.getBalance()

Hemlal.deposite(85484)

Hemlal.withdraw(10000)

Dulal.transfer(10000, Hemlal)

Hem = InterestRewardsAcct(1000, "Hem")
Hem.getBalance()
Hem.deposite(100)
Hem.transfer(100, Dulal)

HemDulal = SavingAcct(5000, "HemDulal")
HemDulal.getBalance()
HemDulal.deposite(500)
HemDulal.transfer(800, Dulal)
HemDulal.transfer(100, Dulal)
