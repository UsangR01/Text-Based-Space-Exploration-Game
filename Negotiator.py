import random
import time
from pprint import pprint           #pprint = pretty printing used to display class info in an easy way
delay=0.5

class negotiator:

    def __init__(self, name):
        self.name = name
        self.health = 5
        self.negotiator_bag = {}
        self.bonus = random.randint(3, 20)
        #self.negotiator_dict = {self.negotiator_bag[i]: self.negotiator_bag[i + 1] for i in range(0, len(self.negotiator_bag), 2)}
        # self. bonus = input("Press enter to spin the bonus wheel: " f'{random.randint(3, 10)}')

    def dropHealth(self):
        """ Negotiator loosing one health (value) from the initialized 5"""
        self.health -= 1

    def getHealth(self):
        """ Negotaitor picking up an extra health"""
        if self.health < 5:
            self.health += 1
        else:
            self.health = 5

    def showHealth(self):
        return f'Life in the bank: {self.health}'

    def healthStatus(self):
        if self.health > 0:
            return
        else:
            print('You are out of Life!')
            time.sleep(0.5)
            print('Game Over')
            return quit()

    def show_negotiator_inv(self):
        """
        Print out name, life and the content in negotiator bag
        """
        return f'Name: {self.name}, Bag: {self.negotiator_bag}, Life: {self.health}, Bonus: {self.bonus}'

    time.sleep(1)