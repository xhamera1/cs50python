def main():
    while True:
        try:
            inp = input("Fraction: ")
            percent = convert(inp)
            res = gauge(percent)
            print(res)
            break

        except (ValueError, ZeroDivisionError):
            pass


def convert(inp):
    x, y = map(int, inp.split("/"))
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)

def gauge(result):
    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{int(round(result))}%"


if __name__ == "__main__":
    main()
