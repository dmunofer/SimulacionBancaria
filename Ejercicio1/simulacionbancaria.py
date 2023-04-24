import threading
from multiprocessing import Manager, Pool

class Account:
    def __init__(self, amount=0):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0

    def transfer(self, dest, amount):
        withdrawn = self.withdraw(amount)
        dest.deposit(withdrawn)

class Bank:
    def __init__(self, num_accounts=1, initial_balance=0):
        self.accounts = [Account(initial_balance) for _ in range(num_accounts)]
        self.manager = Manager()

    def random_transfer(self, num_transfers):
        def _transfer():
            src, dest = self.manager.choice(self.accounts, size=2, replace=False)
            amount = self.manager.choice([20, 50, 100])
            src.transfer(dest, amount)

        pool = Pool(processes=4)
        pool.map_async(lambda x: _transfer(), range(num_transfers))
        pool.close()
        pool.join()

    def check_balance(self):
        total_balance = sum([account.balance for account in self.accounts])
        return total_balance

if __name__ == '__main__':
    NUM_ACCOUNTS = 10
    INITIAL_BALANCE = 100
    NUM_TRANSFERS = 1000

    with Manager() as manager:
        bank = Bank(num_accounts=NUM_ACCOUNTS, initial_balance=INITIAL_BALANCE)

        # Ingreso de dinero inicial en las cuentas
        for account in bank.accounts:
            account.deposit(INITIAL_BALANCE)

        # Transferencia aleatoria de dinero entre cuentas
        bank.random_transfer(NUM_TRANSFERS)

        # Comprobación de saldo total
        total_balance = bank.check_balance()

        # Verificación de saldo final
        assert total_balance == NUM_ACCOUNTS * INITIAL_BALANCE, f'Saldo final incorrecto: {total_balance}'
        print('¡La simulación bancaria ha finalizado con éxito!')
