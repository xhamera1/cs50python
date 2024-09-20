import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        filename_before = sys.argv[1]
        filename_after = sys.argv[2]
        if not filename_before.endswith(".csv"):
            sys.exit(f"Could not read {filename_before}")
        if not filename_after.endswith(".csv"):
            sys.exit(f"Could not read {filename_after}")
        with open(filename_before, "r") as file_before, open(filename_after, "w", newline="") as file_after:
            reader = csv.reader(file_before)
            writer = csv.DictWriter(file_after, fieldnames=["first", "last", "house"])

            next(reader)

            writer.writeheader()

            for row in reader:
                full_name, house = row
                surname, name = full_name.split(", ")
                writer.writerow({"first": name, "last": surname, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {filename_before}")

if __name__ == "__main__":
    main()
