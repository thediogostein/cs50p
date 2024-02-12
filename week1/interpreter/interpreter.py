def main():
    expression = input("Expression: ")

    x, y, z = expression.split()

    result = calculate(int(x), y, int(z))

    print(round(result, 1))


def calculate(n1, operator, n2):
    match operator:
        case "+":
            return float(n1 + n2)
        case "-":
            return float(n1 - n2)
        case "/":
            return float(n1 / n2)
        case "*":
            return float(n1 * n2)


main()
