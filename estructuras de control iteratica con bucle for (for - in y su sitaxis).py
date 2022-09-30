## Estructura de control iterativa for - in

## Bucle For - definición:
# significa (para una variable dentro de una iterable).
## que puede ser una: Lista, Una tupla, una cadena entre otros
## y trabaja de la siguiente manera.

## para var (variable) dentro <iterable>------------> (son lista,tuplas,diccionarios, conjuntos o cadenas):
##    accion 1
#     accion N

## la variable va tomando los valores dentros del iterable
## uno a la vez, por cada iteracion del bucle FOR (OSEA POR CADA VUELTA QUE DE EL CICLO O BUCLE)
## hasta llegar al ultimo elemento del iterable, al momento de leer el ultimo elemento
## del iterable termina el ciclo.




#for con lista

for n in [1,2,3,4,5]:
    c=n*n
    print(n,c)

#for con tuplas

colores = ("amarillo", "azul", "rojo", "blanco")
for c in colores:
   print(c)

#for con cadena
academia = "G-Talent"
for c in academia:
    print (c)