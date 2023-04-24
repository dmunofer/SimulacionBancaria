import random

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bet(self, number, casino):
        bet_type = random.choice(['number', 'even_odd', 'martingale'])
        if bet_type == 'number':
            self.number_bet(number, casino)
        elif bet_type == 'even_odd':
            self.even_odd_bet(number, casino)
        elif bet_type == 'martingale':
            self.martingale_bet(number, casino)

    def number_bet(self, number, casino):
        chosen_number = random.randint(1, 36)
        if chosen_number == number:
            self.balance += 360
            casino.bank -= 360
        else:
            self.balance -= 10
            casino.bank += 10

    def even_odd_bet(self, number, casino):
        is_even = number % 2 == 0
        chosen_bet = random.choice(['even', 'odd'])
        if is_even and chosen_bet == 'even':
            self.balance += 20
            casino.bank -= 20
        elif not is_even and chosen_bet == 'odd':
            self.balance += 20
            casino.bank -= 20
        else:
            self.balance -= 10
            casino.bank += 10

    def martingale_bet(self, number, casino):
        chosen_number = random.randint(1, 36)
        bet = 10
        while True:
            if chosen_number == number:
                self.balance += bet * 36
                casino.bank -= bet * 36
                break
            else:
                self.balance -= bet
                casino.bank += bet
                bet *= 2
                if self.balance < bet:
                    bet = self.balance
