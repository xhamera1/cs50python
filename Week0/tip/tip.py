def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    res = d[1:]
    res = float(res)
    return res



def percent_to_float(p):
    # TODO
    res = p[:2]
    res = float(res)/100
    return res


main()
