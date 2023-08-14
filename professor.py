"""
Progam prompts user for difficulty of 1 - 3.
User will answer 10 questions and gets 3 tries per question to get it correct
After 10 questions, program will spit out a score
"""
import random


def main():
    # ask user for level of difficulty
    level = get_level()

    # inialize total num  of questions, tries and score
    num_quest = 10
    tries = 3
    score = 0

    for i in range(num_quest):
        # generate an x and y
        x = generate_integer(level)
        y = generate_integer(level)

        # get correct answer
        correct = x + y

        j = 0

        # give player 3 tries to get the correct answer
        while j <= tries:
            # add a try
            j += 1

            # print question
            print(f"{x} + {y} = ", end="")

            # if answer isn't a number, raise an exception, if it is, break out of current loop
            try:
                ans = int(input().strip())
                if ans == correct:
                    score += 1
                    break
            except ValueError:
                pass

            # if answer isn't correct print EEE, if this is the 3rd try, provide the correct answer
            print("EEE")
            if j == tries:
                print(f"Correct answer: {x} + {y} = {correct}")
                break

    # print total score
    print(f"Score: {score}")


def get_level():
    # Get an input from the user. Only n of 1, 2, or 3 are accepted
    while True:
        num_list = [1, 2, 3]
        try:
            n = int(input("Level: ").strip())
            if n in num_list:
                return n

        except ValueError:
            pass



def generate_integer(level):
    # depending on the level user inputted, generate an integer
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
