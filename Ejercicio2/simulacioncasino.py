import random
import time
import threading

class Casino:
    def __init__(self):
        self.bank = 50000
        self.players = [Player(str(i), 1000) for i in range(1, 17)]
        self.lock = threading.Lock()

    def play(self):
        while True:
            number = random.randint(0, 36)
            for player in self.players:
                threading.Thread(target=player.bet, args=(number, self.lock)).start()
            time.sleep(3)

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bet(self, number, lock):
        bet_type = random.choice(['number', 'even_odd', 'martingale'])
        with lock:
            if bet_type == 'number':
                self.number_bet(number)
            elif bet_type == 'even_odd':
                self.even_odd_bet(number)
            elif bet_type == 'martingale':
                self.martingale_bet(number)

    def number_bet(self, number):
        chosen_number = random.randint(1, 36)
        if chosen_number == number:
            self.balance += 360
            with self.lock:
                casino.bank -= 360
        else:
            self.balance -= 10
            with self.lock:
                casino.bank += 10

    def even_odd_bet(self, number):
        is_even = number % 2 == 0
        chosen_bet = random.choice(['even', 'odd'])
        if is_even and chosen_bet == 'even':
            self.balance += 20
            with self.lock:
                casino.bank -= 20
        elif not is_even and chosen_bet == 'odd':
            self.balance += 20
            with self.lock:
                casino.bank -= 20
        else:
            self.balance -= 10
            with self.lock:
                casino.bank += 10

    def martingale_bet(self, number):
        chosen_number = random.randint(1, 36)
        bet = 10
        while True:
            if chosen_number == number:
                self.balance += bet * 36
                with self.lock:
                    casino.bank -= bet * 36
                break
            else:
                self.balance -= bet
                with self.lock:
                    casino.bank += bet
                bet *= 2
                if self.balance < bet:
                    bet = self.balance

if __name__ == '__main__':
    casino = Casino()
    for i in range(4):
        threading.Thread(target=casino.play).start()
