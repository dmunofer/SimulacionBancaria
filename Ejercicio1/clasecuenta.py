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