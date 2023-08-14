"""
Progam prompts user for difficulty of 1 - 3.
User will answer 10 questions and gets 3 tries per question to get it correct
After 10 questions, program will spit out a score
"""
import random


def main():
    level = get_level()
    num_quest = 3
    tries = 3
    # prompt user to solve questions
    score = 0
    questions = 0
    i = 0

    while i < num_quest:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            print(f"{x} + {y} = ", end="")
            ans = int(input().strip())
            correct = x + y
            if ans != correct:
                raise Exception()
            j = 1
            while j <= tries:
                try:
                    if ans != correct:
                        print("EEE")
                        if j == tries:
                            print(f"{x} + {y} = {correct}" )
                            score -= 1
                            break
                        print(f"{x} + {y} = ", end="")
                        ans = int(input().strip())
                        if ans == correct:
                            break
                        j += 1
                    else:
                        break
                except ValueError:
                    pass

            score += 1
            questions +=1
            if questions == num_quest:
                break
        except:
            pass


    print(f"Score: {score}")

def get_level():
    # Get an input from the user. Only n of 1, 2, or 3 are accepted
    while True:
        try:
            n = int(input("Level: ").strip())
            if n < 1 or n > 3:
                pass
            else:
                return n
        except ValueError:
            pass

def generate_integer(level):
    # depending on the level user inputted, generate an integer
    match level:
        case 1:
            return(random.randint(0, 9))
        case 2:
            return(random.randint(10, 99))
        case 3:
            return(random.randint(100, 999))

if __name__ == "__main__":
    main()