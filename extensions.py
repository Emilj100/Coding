name = input().strip().lower()

match name:
    case ".jpg":
        print("image/jpeg")
    case ".gif":
        print("image/gif")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("image/pdf")
    case ".txt":
        print("image/txt")
    case ".zip":
        print("image/zip")
    case _:
        print()

