import random
import time
import threading
from player import Player

class Casino:
    def __init__(self):
        self.bank = 50000
        self.players = [Player(str(i), 1000) for i in range(1, 17)]
        self.lock = threading.Lock()

    def play(self):
        while True:
            number = random.randint(0, 36)
            for result in map(lambda player: player.bet(number, self), self.players):
                pass
            time.sleep(3)

