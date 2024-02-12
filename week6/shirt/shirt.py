from sys import argv
from sys import exit
from PIL import Image, ImageOps
import os


def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")

    source_name, source_extension = os.path.splitext(argv[1])
    output_name, output_extension = os.path.splitext(argv[2])

    source_file = f"{source_name}{source_extension}"
    output_file = f"{output_name}{output_extension}"

    if not validate_extension(source_extension):
        exit("Invalid input")
    if not validate_extension(output_extension):
        exit("Invalid output")
    if not are_equal_extension(source_extension, output_extension):
        exit("Input and output have different extensions")

    overlay_images(source_file, output_file)


def validate_extension(ext):
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if ext in valid_extensions:
        return True
    else:
        return False


def are_equal_extension(source, output):
    if source == output:
        return True
    else:
        return False


def overlay_images(input, output):
    # Open input image
    try:
        input_image = Image.open(input)
    except FileNotFoundError:
        exit("Input does not exist")

    # Open shirt image
    try:
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        exit("Shirt.png does not exist")

    # Get size of the shirt image
    shirt_size = shirt_image.size

    # Resize and crop the input image
    resized_input = ImageOps.fit(input_image, shirt_size)

    # Overlay the shirt image on the input image
    resized_input.paste(shirt_image, (0, 0), shirt_image)

    # Save the result as the output image
    resized_input.save(output)


if __name__ == "__main__":
    main()
