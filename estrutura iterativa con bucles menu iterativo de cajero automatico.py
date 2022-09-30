##estrutura de control iterativas con bucles
##menu iterativo cajero automatico.
##
###
##se realizo un caso practico aplicando estrutras de control iterativa
##while controlada por un evento y se empleo la instruccion break
#
  #cajero automatico con menu interativo

from random import randrange

saldo = randrange(0,5000000)

print( " **** bienvenido al cajero automatico del banco bhd león " )

print("\n operaciones disponibles")

while True:   #ciclo bucles

  print("\n 1. saldo")
  print("\n 2. retiro")
  print("\n 3. deposito")
  print("\n 0. salir ")

  opcion =int(input("elija una operacion a realizar por favor entre los numero [0 y 3] : "))
  if opcion in range (4):
        if opcion == 1:
            print("su saldo actual es de: ", saldo)
        elif opcion == 2:
            monto = int(input(" por favor indique el monto a retirar: "))
            if monto > saldo:
              print(" operacion invalidad, saldo insuficiente")
            else:
              saldo = saldo - monto
              print("operacion exitosa! ")
              print (" su saldo actual es: " , saldo)
        elif opcion == 3:
              monto = int(input(" indque el monto a depositar: "))
              saldo = saldo + monto
              print(" su saldo alctual es: ", saldo)
        else:
                print("hasta luego ...")
                break
else:
        print(" la opcion seleccionada no esta ddisponible ")
