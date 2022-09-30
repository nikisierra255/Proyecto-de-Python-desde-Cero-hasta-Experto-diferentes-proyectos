#contar vocales cada una en cadena, caso practico

cadena = input("ingrese una oracion: ")

vocales =["a", "e", "i", "o","u"]

print ("\n la cantidad de voclaes son: ")

for  i in range(len(vocales)):
    print("\t", vocales [i], "---->", cadena.count(vocales[i]))


# se realizo un caso practico de cadena