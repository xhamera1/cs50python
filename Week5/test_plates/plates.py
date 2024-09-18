def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    if len(str)>6 or len(str)<2 :
        return False
    if str[0].isalpha() == False or str[1].isalpha() == False :
        return False
    numbers_started = False
    for i in range(len(str)):
        if str[i].isalnum() == False :
            return False
        if numbers_started == True and str[i].isalpha() == True:
            return False
        if numbers_started == False and str[i].isnumeric():
            numbers_started = True
            if str[i] == "0":
                return False
    return True


if __name__ == "__main__":
    main()
