#comprobando vocales

Letra = input("indique una Letra: ")

if Letra == "a" or Letra == "e" or Letra == "i" or Letra == "o" or Letra =="u":
    print("la Letra", Letra, "es vocal y minuscula")

elif Letra == "A" or Letra == "E" or Letra == "I" or Letra == "O" or Letra =="U":
    print("La Letra", Letra, "es vocal y mayuscula")

else:
    print("La Letra", Letra, "es una consonante")