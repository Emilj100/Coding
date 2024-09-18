name = input("hi").strip().lower()

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg"):
    print("image/jpeg")
elif name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("image/pdf")
elif name.endswith(".txt"):
    print("image/txt")
elif name.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")
