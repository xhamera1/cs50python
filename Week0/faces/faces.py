def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁 ")
    return text



def main():
    str = input()
    print(convert(str))

main()
