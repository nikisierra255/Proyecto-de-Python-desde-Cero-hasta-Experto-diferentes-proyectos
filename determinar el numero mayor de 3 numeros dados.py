#determinar el mayor de 3 numeros dados

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercel numero entero: "))
if num1 > num2 and num1 > num3:
    print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num1))
elif num2 > num1 and num2 > num3:
    print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num2))
else:
    print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num3))

#si los 3 numeros son iguales se le debe de agregar otra estrutura condicional if

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercel numero entero: "))
if num1 != num2 and num1 != num3 and num2 != num3:
   if num1 > num2 and num1 > num3:
     print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num1))
   elif num2 > num1 and num2 > num3:
     print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num2))
   else:
     print("de {}, {}, {} el mayoe es {}". format (num1,num2,num3,num3))
else:
    print("existen 2 o mas numeros iglaes, por lo tanto no hay numero mayor")