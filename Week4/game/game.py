import random
import sys

class NonPositiveError(Exception):
    pass

while True:
    try:
        level = int(input("Level: "))
        if level <= 0 :
            raise NonPositiveError()
        random_number = random.randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0 :
                    raise NonPositiveError()
                if guess < random_number:
                    print("Too small!")
                elif guess > random_number:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit(0)

            except (ValueError, NonPositiveError):
                pass



    except (ValueError, NonPositiveError):
        pass
