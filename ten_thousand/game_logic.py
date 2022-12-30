import random
from collections import Counter
from play import validate_keepers


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """method which will return you n random integers between 1 - 6"""
        roll = []
        for x in range(n):
            roll.append(random.randint(1, 6))
        roll = tuple(roll)
        return roll

    @staticmethod
    def calculate_score(roll):
        """takes dice rolls as an input and returns an integer representing the roll's score """
        current_score = 0
        # dummy roll if needed
        # roll = (1, 1, 1, 1, 1, 1)
        roll = sorted(roll)
        counted_roll = Counter(roll)
        Counter.elements(counted_roll)
        as_list = list(counted_roll.items())

        # straight - 1,2,3,4,5,6 should return correct score
        # can also examine length here len(as_list) == 6
        if as_list == [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]:
            current_score += 1500
            as_list = []

        # three_pairs - 3 pairs should return correct score, can clean up equalities too
        if len(as_list) == 3 and as_list[1][1] == 2 and as_list[0][1] == 2:
            current_score += 1500
            as_list = []

        # two_trios - 2 sets of 3 should return correct score, can clean up equalities too
        if len(as_list) == 2 and as_list[0][1] == 3 and as_list[1][1] == 3:
            for i, j in as_list:
                if j > 2 and i == 1:
                    current_score += 1000
                if j > 2 and i >= 2:
                    current_score += i*100*(j-2)
                    as_list = []

        for i, j in as_list:
            # zilch - roll with no scoring dice should return 0
            # ones - rolls with various number of 1s should return correct score
            if j > 2 and i == 1:
                current_score += 1000 * (j - 2)
            # twos - rolls with various number of 2s should return correct score
            # threes - rolls with various number of 3s should return correct score
            # fours - rolls with various number of 4s should return correct score
            # fives - rolls with various number of 5s should return correct score
            # sixes - rolls with various number of 6s should return correct score
            elif j > 2 and i >= 2:
                current_score += i * 100 * (j - 2)
            # leftover_ones - 1s not used in set of 3 (or greater) should return correct score
            elif j < 3 and i == 1:
                current_score += j * 100
            # leftover_fives - 5s not used in set of 3 (or greater) should return correct score
            elif j < 3 and i == 5:
                current_score += j * 50

        return current_score
