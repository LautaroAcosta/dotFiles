def division(x, y):
    if x < y:
        return 0
    else:
        return 1 + division(x-y, y)


x = input("Ingrese el dividendo: ")
y = input("Ingrese el divisor: ")
print(division(int(x), int(y)))
