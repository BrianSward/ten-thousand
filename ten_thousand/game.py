from config import greeting
from game_logic import GameLogic
from random import randint


def default_roller():
    return randint(1, 6), randint(1, 6)


# noinspection SpellCheckingInspection
def play_dice(roller=default_roller):
    """
    this function handles the logic to the playing of the game ten thousand
    """
    round_ = 0
    is_game = True
    while is_game:
        print(greeting)
        choice = input("> ")
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
                print(f"Rolling {dice_num} dice...")
                roll_str = ""
                for num in roll:
                    roll_str += str(num) + " "
                print(f"*** {roll_str} ***")
                if GameLogic.calculate_score(tuple(roll)) == 0:
                    print("Zilch! You Lose and Must start again!")
                    break
                print("Enter dice to keep, or (q)uit:")
                dice = input("> ")
                if dice == "q":
                    print(f"Thank you for playing. You earned {total_score} points")
                    is_game = False
                    break
                keep_list = []
                for i in dice:
                    keep_list.append(int(i))
                dice_num -= len(keep_list)
                unbanked_score += GameLogic.calculate_score(tuple(keep_list))
                print(f"You have {unbanked_score} unbanked points"
                      f" and {dice_num} dice remaining")
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
                    print(f"Thank you for playing. You earned {total_score} points")
                    is_game = False
                    break
            if round_ > 5:
                print("Game Over! Set Number of Rounds Exceeded")
                print(f"Total Score: {total_score}")
                print(f"After {round_-1} rounds.")
                is_game = False


if __name__ == '__main__':
    rolls = [(5, 6), (6, 1)]

    def mock_roller():
        return rolls.pop(0) if rolls else default_roller()


    play_dice(mock_roller)
