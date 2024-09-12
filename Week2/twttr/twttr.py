str = input("Input: ")
result_string = ""
for i in range(len(str)):
    if str[i].lower() not in ["a", "e", "i", "o", "u"]:
        result_string += str[i]
print(f"Output: {result_string}")


