#comprobando vocales

letra = input("indique una letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
   print("la letra" , letra, "es vocal y es minuscula")
elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
   print("la letra" , letra, "es vocal y es mayuscula")
else:
    print("la letra" , letra, "es una consonante")