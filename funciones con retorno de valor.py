def suma_cuadrado(* numeros):
    cuad = 0
    for num in numeros:
        cuad += num **2
    return cuad
sc =suma_cuadrado(1,2,3)
print("la suma de los primeros numeros cuadrados es: " , sc)