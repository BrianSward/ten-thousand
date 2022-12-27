# worked with cody delatorre to achieve this code
import random


class GameLogic:

    def roll_dice(n):
        """method which will return you n random integers between 1 - 6"""
        roll = []
        for x in range(n):
            roll.append(random.randint(1, 6))
        roll = tuple(roll)
        return roll

    def calculate_score(self):
        pass
