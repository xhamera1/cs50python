def value(word):
     word = word.lower()
     if word[:5]=="hello":
        return 0
     elif word[0]=="h":
        return 20
     else:
        return 100


def main():
    greeting = input("Greeting: ").lower().strip()
    words = greeting.split()
    word = words[0]
    val = value(word)
    print(f"${val}")



if __name__ == "__main__":
    main()
