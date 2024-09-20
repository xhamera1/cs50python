import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        filename1, extension1 = sys.argv[1].split(".")
        filename2, extension2 = sys.argv[2].split(".")
        if extension1!=extension2:
            sys.exit("File extensions must be the same")
        ext = ["jpg", "jpeg", "png"]
        if extension1.lower() not in ext:
            sys.exit(f"Wrong extension of {sys.argv[1]}")
        if extension2.lower() not in ext:
            sys.exit(f"Wrong extension of {sys.argv[2]}")
        with Image.open(sys.argv[1]) as image:
            with Image.open("shirt.png") as shirt:
                shirt_width, shirt_height = shirt.size
                image = ImageOps.fit(image, size=(shirt_width,shirt_height))
                image.paste(shirt,(0,0), shirt)
                image.save(sys.argv[2])


    except ValueError:
        sys.exit("Wrong filenames")



if __name__ == "__main__":
    main()
