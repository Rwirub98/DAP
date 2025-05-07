import numpy as np

a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 2], [4, 5]])

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Dot product")
    print("6. Exponentiation")
    print("7. Logarithm (base e)")
    print("8. Logarithm (base 10)")
    print("9. Exit")

    n = int(input("Enter the option number: "))

    if 1 <= n <= 9:
        if n == 1:
            c = np.add(a, b)
            print("Sum:\n", c, "\n")
        elif n == 2:
            d = np.subtract(a, b)
            print("Difference:\n", d, "\n")
        elif n == 3:
            e = np.multiply(a, b)
            print("Product:\n", e, "\n")
        elif n == 4:
            f = np.divide(a, b)
            print("Quotient:\n", f, "\n")
        elif n == 5:
            g = np.dot(a, b)
            print("Dot product:\n", g, "\n")
        elif n == 6:
            h, i = np.exp(a), np.exp(b)
            print("Exponentiation of array a:\n", h)
            print("Exponentiation of array b:\n", i, "\n")
        elif n == 7:
            l, m = np.log(a), np.log(b)
            print("Natural logarithm (base e) of array a:\n", l)
            print("Natural logarithm (base e) of array b:\n", m, "\n")
        elif n == 8:
            x, y = np.log10(a), np.log10(b)
            print("Logarithm (base 10) of array a:\n", x)
            print("Logarithm (base 10) of array b:\n", y, "\n")
        elif n == 9:
            print("Exiting...")
            break
    else:
        print("No such option exists, please enter a valid option.\n")
