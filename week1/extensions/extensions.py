def main():
    file_name = input("File name: ")
    print(get_file_type(file_name))


def get_file_type(name):

    type = name.split(".")

    if len(type) >= 2:
        extension = type[-1].lower().strip()
    else:
        extension = "_"


    match extension:
        case "jpg" | "jpeg":
            return f"image/jpeg"
        case "gif" | "png":
            return f"image/{extension}"
        case "pdf" | "zip":
            return f"application/{extension}"
        case "txt":
            return f"text/plain"
        case _:
            return f"application/octet-stream"


main()
