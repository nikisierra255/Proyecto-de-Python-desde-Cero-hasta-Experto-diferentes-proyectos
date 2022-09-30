

             #COLECCIONES -PILAS

#PILA ES UN TIPO DE DATO ABSTRACTO EN LA CUAL SE APILA (INSERTA) Y DESAPILA (ELIMINA)
#ELEMENTOS POR UN SOLO EXTREMO QUE SE DENOMICA (TOPE O CIMA)
#Y LA ACCION DE DESAPILAR (POP) LOS ELEMENTOS, SOLO SE PUEDE REALIZAR EN ORDEN INVERSO
#QUE SE INSERTA EN LA PILA(PUSH) # OJO: EL ULTIMO ELEMENTO QUE SE PONE EN LA PILA
#ES EL PRIMER ELEMENTO QUE SE DEBE SACAR.
# POR ESTO A ESTA ESTRUCTURA LINEAL SE LE CONOCE COMO
#(LIFO (LAST-IN, FIRST-OUT) ULTIMO EN ENTRAR, PRIMERO EN SALIR).

#PILAS Y SUS OPERACIONES: APILAR, DESAPILAR, VACIA Y MOSTRAR SU CONTENIDO

from collections import deque
#declaracion pila

pila = deque()

i=0
while True:
    i+=1
    # apila elementos
    pila.append ("elemento {}".format(i))
    print ("\n se agrego un elemento a la pila")
    #mostrar la pila
    print("\n ", pila)
    if input ("desea apilar otro elemento [s/n]: ") == "n":
        break
#mostar la pila
print ("{}".format(pila))

while len(pila) > 0:
    #desapilar elementos
    elemento = pila.pop()
    print("\n elemento desapilado {}".format(elemento))

#mostrar pila
print(pila)