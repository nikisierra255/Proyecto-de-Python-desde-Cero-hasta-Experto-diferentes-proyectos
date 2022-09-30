#CALCULADORA ARITMETICA

print ("*** calculadora aritmetica ***")

print("operaciones que puede realizar: \" + , - , * , /\"")
operacion = input ("selecione la operacion: ")
x = int(float(input("ingrese un valor: ")))
y = int(float(input("ingrese otro valor: ")))
if operacion == '+' :
    print("la suma es: ", x+y)
elif operacion== '-' :
    print("la resta es: ", x-y)
elif operacion == '*' :
    print("la multiplicacion es: ", x*y)

else:
    if y !=0:
      print("la division es: ", x/y)
    else:
      print("la operacion no se puede realizar, debido a que el divisor es 0")
