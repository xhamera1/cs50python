while True:
    try:
        inp = input("Fraction: ")
        x, y = map(int, inp.split("/"))
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        result = float(x) / float(y)
        if result <= 0.01:
            print("E")
            break
        elif result >= 0.99:
            print("F")
            break
        else:
            print(f"{result:.0%}")
            break

    except ValueError or ZeroDivisionError:
        pass


