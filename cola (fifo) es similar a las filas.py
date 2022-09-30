#colecciones de datos colas.

#la cola es un tipo de estructura lineal similar a la fila.

# cola es un tipo de datos abtracto, en la cual la insercion
# de elemento se ralizapor por el extremo final (push - encolar)
# y la eliminacion de elemnto se realiza por el extremo iniciar (pop - desencolar)
# en las colas el elemto que entro primero, tambien sale primero, por ello a estas estructura se le denomina
# FIFO( first-in, First-Out) primero en entrar, primero en salir.


#cola y las operaciones, desencolar, cola vacia y mostrar contenido.

from collections import deque

#declaracion de cola
cola = deque()

i=0

while True:
    i+=1
    #encolar elemtos
    cola.append("elemento {}".format(i))
    print("\n se agrego un elemento a la cola")
    print (cola)

    if input("desea encolar otro elemnto [s/n]") == "n":
        break

print("*** COLA***")
print("cola")

#desencolar los elemntos

while len(cola) > 0:
    #desencolar elemento
    elemento = cola.popleft()
    print("elemento desencolado {}".format(elemento))

    #mostrar cola

    print (cola)
