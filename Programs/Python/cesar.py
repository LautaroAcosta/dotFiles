

def cesar (text,key):
    x = ""  
    for i in range(len(text)):
        x = text[i]
        if (x.isupper() == True):
            a = ord(x)+key
            #65-90
            while (a > 90):
                s = a - 90
                a = 65 + s
            
            x += chr(a)

        elif (x.islower() == True):
        #97-122
            a = ord(x)+key
            #65-90
            while (a > 122):
                s = a - 122
                a = 97 + s   

            x +=chr(a)
        
    return x

text = input("Ingrese una cadena de texto: ")
key= int(input("Ingrese el desplazamiento: "))

print (cesar(text,key))
