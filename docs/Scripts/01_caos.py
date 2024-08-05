# caos.py
# Un programa que ilustra una conducta caótica


def main():
    print("Este programa ilustra una función caótica")
    x = eval(input("Ingresa un número entre 0 y 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


main()
