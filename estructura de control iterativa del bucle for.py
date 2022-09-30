### bucle o ciclo (FOR)
##
### DEFINICION
##
## EL BUCLE FOR SIGNIFICA (PARA UNA VARIABLE DENTRO DE UN ITERABLE)
## QUE PUEDE SER UNA LISTA, UNA TUPLA O UNA CADENA ENTRE OTROS
## Y TRABAJA DE LA SIGUIENTE MANERA LA VARIABLE VA TOMANDO LOS VALORES DE LOS ELEMENTOS ITERABLE
## UNO A LA VEZ , POR CADA ITERACION DEL FOR, HASTA LLEGAR AL ULTIMO DEL ELEMENTO DEL ITERABLE

#SINTAXIS

##for <variable>(toma el elemento dentro del iterador) in <iterable>(lista,tuplas,diccionarios, conjuntos o cadenas):
##    accion a realizar
##
##
##    accion a terminar
##
##    hasta que se recorra el ultimo elemento iterador






#for con listas

for n in [1,2,3,4,5]:
    c=n**n
    print (n,c)



#for con tuplas

colores = ("amarillo","azul ", "rojo","blanco")
for c in colores:
  print (c)


#for con cadena
academia = "g-talent"
for c in academia:
    print(c)



