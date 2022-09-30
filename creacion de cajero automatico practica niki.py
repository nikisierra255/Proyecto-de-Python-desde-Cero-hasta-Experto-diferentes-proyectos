#cajero automatico

from random import randrange

#dame un numero aleatorio entre 0 y 5,000,000 millones

saldo = randrange(0,5000000)

#mensaje de bienvenida

print("*******bienvenido al cajero atm bhd*******")
print()
print("opciones disponibles: ")
print()
print ("1. consulta de saldo disponible")
print()
print("2. extraer dinero")
print()
print("3. depositar dinero")
print()
print("4. transferencia")
print()
print("0. salir")

opcion = int(input("seleccione la opcion a realizar: "))
# confirmar que las opciones digitada por el usuario debe de estar dentro del rango del 0 a 4 (osea 5)
if opcion in range(5):
    if opcion == 0:
        print("hasta luego...")
    elif opcion == 1:
        print("su saldo disponible es ", saldo)
    elif opcion == 2:
        monto = int(input("indique el monto a retirar"))
        if monto > saldo:
           print("saldo no disponible")
        else:
            saldo = saldo - monto
            print("retire si dinero del dispensador")
            print("su saldo actul es: ", saldo)
    elif opcion == 3:
        monto = int(input("indique el monto a depositar: "))
        saldo = saldo + monto
        print("su saldo actual es: ", saldo)
    else:
        cuenta = int(input("ingrese numero de cuenta a trasnferir: "))
        monto = int(input("indique el monto a transferir: "))
        if monto > saldo:
            print("la operacion no se ejecuto, por saldo insuficiente")
        else:
            print("transferencia realizada con exito")
            saldo = saldo - monto
            print("su saldo actual es: ", saldo)

