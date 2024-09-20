import sys

def main():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    else:
        try:
            count = 0
            filename = sys.argv[1]
            if filename[-3:]==".py":
                pass
            else:
                sys.exit("Not a Python file")
            file = open(sys.argv[1], "r")
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line[0] == '#':
                    continue
                count += 1
            file.close()
            print(count)
        except OSError:
            sys.exit("error")


if __name__ == "__main__":
    main()
