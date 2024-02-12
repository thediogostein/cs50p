def main():
    user_input = input()
    result = convert(user_input)
    print(result)


def convert(str):
    return str.replace(':)', '🙂').replace(':(', '🙁')


main()
