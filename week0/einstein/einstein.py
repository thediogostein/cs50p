def main():
    mass = int(input("m: "))
    result = converter(mass)
    print(f"E: {result}")


def converter(m):
    return  m * pow(300_000_000, 2)


main()
