greeting = input("Greeting: ").lower().strip()
words = greeting.split()
print(words)
word = words[0]
if word[:5]=="hello":
    print("$0")
elif word[0]=="h":
    print("$20")
else:
    print("$100")
