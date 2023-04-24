from multiprocessing import Pool, Manager
from clasebanco import *
from clasecuenta import *
from run import *



if __name__ == '__main__':
    manager = Manager()
    bank = Bank()
    account1 = Account("Account1", bank)
    account2 = Account("Account2", bank)

    p = Pool(processes=4)
    p.map(run_bank, [bank, bank, bank, bank])

    bank.check_balance()
