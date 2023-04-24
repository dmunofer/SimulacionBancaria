from clasebanco import *
from clasecuenta import *


def run_bank(bank):
    for _ in range(40):
        bank.deposit(100)
        bank.withdraw(100)
    for _ in range(20):
        bank.deposit(50)
        bank.withdraw(50)
    for _ in range(60):
        bank.deposit(20)
        bank.withdraw(20)