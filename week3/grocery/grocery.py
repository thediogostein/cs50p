def main():
    order_dic = {}

    while True:
        try:
            item = get_input()
            add_to_list(item, order_dic)
        except EOFError:
            print("\n")
            break

    sorted_order_dic = dict(sorted(order_dic.items()))
    for item in sorted_order_dic:
        print(order_dic[item], item.upper())


def get_input():
    return input()


def add_to_list(key, dic):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1


if __name__ == "__main__":
    main()
