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

