# determinar el mayor de 3 numeros dados

num1 = int(input("ingrese el primer numero entero: "))

num2 = int(input("ingrese el segundo numero entero: "))

num3 = int(input("ingrese el tercel numero entero: "))

# en caso de los tres numero ser iguales
if num1 != num2 and num1 != num3 and num2 != num3:
#como poder evitar de que eso nos pase en el ejercicio.

  if num1 > num2 and num1 > num3:
   print("de {}, {}, {} el mayor es {}". format(num1,num2,num3,num1))

  elif num2 > num1 and num2 > num3:
   print("de {}, {}, {} el mayor es {}". format(num1,num2,num3,num2))

  else:
   print("de {}, {}, {} el mayor es {}". format(num1,num2,num3,num3))

    # en caso de los tres numero ser iguales
else:
    print("existen 2 o mas nuemros iguales, por lo tanto no hay numero mayor")
#como poder evitar de que eso nos pase en el ejercicio.