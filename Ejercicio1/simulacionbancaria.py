from multiprocessing import Pool, Manager
import threading


class Bank:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount}. Current balance: {self.balance}")
            else:
                print(f"Not enough balance to withdraw {amount}.")

    def transfer(self, amount, account):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                account.deposit(amount)
                print(f"Transferred {amount}. Current balance: {self.balance}")
            else:
                print(f"Not enough balance to transfer {amount}.")

class Account:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def check_balance(self):
        self.bank.check_balance()

    def deposit(self, amount):
        self.bank.deposit(amount)

    def withdraw(self, amount):
        with self.bank.lock:
            self.bank.withdraw(amount)

    def transfer(self, amount, account):
        with self.bank.lock:
            self.bank.transfer(amount, account)


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


if __name__ == '__main__':
    manager = Manager()
    bank = Bank()
    account1 = Account("Account1", bank)
    account2 = Account("Account2", bank)

    p = Pool(processes=4)
    p.map(run_bank, [bank, bank, bank, bank])

    bank.check_balance()
