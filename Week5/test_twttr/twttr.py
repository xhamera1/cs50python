def main():
    str = input("Input: ")
    result_string = shorten(str)
    print(f"Output: {result_string}")


def shorten(str):
    result_string = ""
    for i in range(len(str)):
        if str[i].lower() not in ["a", "e", "i", "o", "u"]:
            result_string += str[i]
    return result_string


if __name__ == "__main__":
    main()
