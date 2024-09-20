import sys
import tabulate
import csv

def main():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    else:
        try:
            filename = sys.argv[1]
            if filename[-4:]==".csv":
                pass
            else:
                sys.exit("Not a CSV file")
            file = open(sys.argv[1], "r")
            reader = csv.reader(file)
            lines = []
            for name, size1, size2 in reader:
                temp = []
                temp.append(name)
                temp.append(size1)
                temp.append(size2)
                lines.append(temp)
            #print(lines)
            print(tabulate.tabulate(lines, headers="firstrow", tablefmt="grid"))
            file.close()
        except OSError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
