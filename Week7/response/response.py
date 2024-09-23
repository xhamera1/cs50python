import validators

inp = input("What's your email adress: ")
if validators.email(inp):
    print("Valid")
else:
    print("Invalid")
