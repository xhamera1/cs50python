input = input("camelCase: ")
result_string = ""
for i in range(len(input)):
    letter = input[i]
    if letter.isupper() == False :
        result_string += letter
    else:
        result_string += "_"
        result_string += letter.lower()

print(f"snake_case: {result_string}")
