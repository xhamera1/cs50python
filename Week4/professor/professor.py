import random

class MyException(Exception):
    pass

def main():
    level = get_level()
    points = 0
    for _ in range(0,10):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        for _ in range(0,3):
            try:
                result = int(input(f"{x} + {y} = "))
                if result == x+y:
                    points += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                    continue
            except ValueError:
                pass
        if tries == 3:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {points}")


def get_level():
    while True:
        validLevel = [1,2,3]
        try:
            level = int(input("Level: "))
            if level not in validLevel:
                raise MyException()
            return level
        except (ValueError, MyException):
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    if level == 2:
        return random.randint(10,99)
    if level == 3:
        return random.randint(100,999)
    return -1 # provided level is invalid


if __name__ == "__main__":
    main()
