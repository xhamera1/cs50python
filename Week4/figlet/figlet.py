import sys
import pyfiglet
import random


if len(sys.argv) == 1:
    inp = input("Input: ")
    f = pyfiglet.Figlet()
    randomFont = random.choice(f.getFonts())
    f.setFont(font=randomFont)
    print(f.renderText(inp))
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    temp = pyfiglet.Figlet()
    if sys.argv[2] not in temp.getFonts():
        sys.exit("Invalid font")
    inp = input("Input: ")
    f = pyfiglet.Figlet(font=sys.argv[2])
    print(f.renderText(inp))
else:
    sys.exit("Invalid usage")
