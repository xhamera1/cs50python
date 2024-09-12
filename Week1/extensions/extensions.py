input = input("File name: ").lower().strip()
first = input.split(".")
second = first[len(first)-1]
if second == "gif":
    print("image/gif")
elif second == "jpeg" or second == "jpg":
    print("image/jpeg")
elif second == "png":
    print("image/png")
elif second == "pdf":
    print("application/pdf")
elif second == "txt":
    print("text/plain")
elif second == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
