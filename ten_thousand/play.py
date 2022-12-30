from config import greeting, zilch
from game_logic import GameLogic
from random import randint


def default_roller():
    return randint(1, 6), randint(1, 6)


def greet(msg):
    print(msg)
    choice = input("> ")
    return choice


def validate_keepers(lock, key):
    """takes incoming roll (lock) and keepers (key) and tests is for all keepers are in lock"""
    scales = False
    for _, x in enumerate(key):
        if key.count(x) == lock.count(x):
            scales = True
        else:
            scales = False
            break
    return scales


# noinspection SpellCheckingInspection
def play_dice(roller):
    """controls the algorythm of the dice game"""
    def roll_call(x):
        """prints out dice rolls as a string"""
        nonlocal roll_str
        for num in x:
            roll_str += str(num) + " "
        print(f"*** {roll_str} ***")

    def quit_outro():
        """prints outro when someone quits"""
        nonlocal is_game
        print(f"Thank you for playing. You earned {total_score} points")
        is_game = False
        return

    choice = None
    round_ = 0
    is_game = True
    while is_game:
        greet(greeting)
        if choice == "n":
            print("OK. Maybe another time")
            is_game = False
        else:
            round_ += 1
            dice_num = 6
            total_score = 0
            unbanked_score = 0
            while 0 < round_ < 6:
                print(f"Starting round {round_}")
                roll = GameLogic.roll_dice(dice_num)
                roll = list(roll)
                dice_num = len(roll)
                check_score = GameLogic.calculate_score(tuple(roll))
                print(f"Rolling {dice_num} dice...")
                roll_str = ""
                roll_call(roll)
                while check_score == 0:
                    print(zilch)
                    unbanked_score = 0
                    roll_str = ""
                    round_ += 1
                    print(f"Starting round {round_}")
                    dice_num = 6
                    print(f"Rolling {dice_num} dice...")
                    roll = GameLogic.roll_dice(dice_num)
                    check_score = GameLogic.calculate_score(tuple(roll))
                    roll_call(roll)
                print("Enter dice to keep, or (q)uit:")
                dice = input("> ")
                if dice == "q":
                    quit_outro()
                    break
                keep_list = [(int(i)) for i in dice if i != " "]
                if validate_keepers(roll, keep_list) is False:
                    print("Cheater!!! Or possibly made a typo...")
                    roll_str = ""
                    roll_call(roll)
                    print("Enter dice to keep, or (q)uit:")
                    dice = input("> ")
                    if dice == "q":
                        quit_outro()
                        break
                    keep_list = [(int(i)) for i in dice if i != " "]
                dice_num -= len(keep_list)
                unbanked_score += GameLogic.calculate_score(tuple(keep_list))
                if dice_num > 0:
                    print(f"You have {unbanked_score} unbanked points"
                          f" and {dice_num} dice remaining")
                if dice_num == 0:
                    print(f"You have {unbanked_score} unbanked points"
                          f" and 6 dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                option = input("> ")
                if option == "r":
                    if dice_num == 0:
                        dice_num = 6
                if option == "b":
                    print(f"You banked {unbanked_score} points in round {round_}")
                    total_score += unbanked_score
                    if total_score >= 10000:
                        print(f"Congrats you win! You scored {total_score}")
                        is_game = False
                        break
                    print(f"Total score is {total_score} points")
                    round_ += 1
                    unbanked_score = 0
                    dice_num = 6
                if option == "q":
                    quit_outro()
                    break
            if round_ > 5:
                print("Game Over! Set Number of Rounds Exceeded")
                print(f"Total Score: {total_score}")
                print(f"After {round_ - 1} rounds.")
                is_game = False


if __name__ == '__main__':
    rolls = [(5, 6), (6, 1)]


    def mock_roller():
        return rolls.pop(0) if rolls else default_roller()


    play_dice(mock_roller)
