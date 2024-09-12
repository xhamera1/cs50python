def convert(time):
    first, second = time.split(":")
    hour = float(first)
    minute = float(second) / 60.0
    return float(hour+minute)


def main():
    inp = input("What time is it? ")
    t = convert(inp)
    if t >= 7.0 and t <= 8.0:
        print("breakfast time")
    elif t >= 12.0 and t <= 13.0:
        print("lunch time")
    elif t >= 18.0 and t <= 19.0:
        print("dinner time")


if __name__ == "__main__":
    main()
