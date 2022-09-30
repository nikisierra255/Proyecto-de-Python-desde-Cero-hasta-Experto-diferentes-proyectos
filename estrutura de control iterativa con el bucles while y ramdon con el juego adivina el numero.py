# estrututa de control iterativa juego de adivina el numero
#el mismo realizado con bucles
##
###se realizo un caso practico aplicando estruturas de control
##iinterativa (while) controlada por una variable contadory se empleo la
##instruccion nreak, el ejercicio consistio en el juego "adivina el numero"
##
###juego adivina el numero

from random import randint

x = randint (1,25)

intentos = 0

while intentos < 6:
    numero = int(input("elige un numero entre 1 y 25 "))
    intentos = intentos + 1

    if numero > x:
        print("tu numero esta por encima")
    elif numero < x:
        print("tu numero esta por debajo")
    else:
        break
if numero == x:
    print("felicitaciones...... eres un genio....")
    print("lo has logrado en {} intentos" . format(intentos))
else:
    print("lo sentimos, has perdido")
    print("no has podido adivinar el numero")
