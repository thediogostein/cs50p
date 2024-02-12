import inflect

p = inflect.engine()

def main():
    names_list = []

    while True:
        try:
            name = input("Name: ")
            names_list.append(name)
        except EOFError:
            mylist = p.join(names_list)
            print(f"\nAdieu, adieu, to {mylist}")
            break


if __name__ == "__main__":
    main()
