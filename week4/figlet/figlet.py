from pyfiglet import Figlet
from sys import argv
from sys import exit
from random import choice


figlet = Figlet()


def main():
    fonts = figlet.getFonts()

    if len(argv) == 1:
        f = choice(fonts)
        figlet.setFont(font=f)
    elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
        if argv[2] in fonts:
            figlet.setFont(font=argv[2])
        else:
            exit("Invalid usage")
    else:
        exit("Invalid usage")

    try:
        user_input = input("Input: ")
        print_figlet(user_input)
    except KeyboardInterrupt:
        exit("\nExiting...")


def print_figlet(str):
    print(figlet.renderText(str))


if __name__ == "__main__":
    main()
