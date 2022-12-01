def Elevar(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a*Elevar(a, b-1)


x = input("Ingrese el numero a elevar: ")
y = input("Ingrese la potencia: ")
print(Elevar(int(x), int(y)))
