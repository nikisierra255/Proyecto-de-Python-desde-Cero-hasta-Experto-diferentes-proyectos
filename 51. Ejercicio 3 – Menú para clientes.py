#menu o gestor parta cliene
global dicccliente
dicccliente = {}

def registrarcliente():
    print ("registrar cliente ")
    idcliente = input("ingrese su cedula: ")
    nombrecliente = input(" ingrese su nombre: ")
    dicccliente[idcliente] = nombrecliente

def listarcliente():
    print ("Listar cliente ")
    idcliente = input("ingrese su cedula: ")
    nombrecliente = input(" ingrese su nombre: ")
    dicccliente[idcliente] = nombrecliente

def buscarcliente():
    print("buscar cliente ")
    idcliente = input("ingrese su cedula: ")
    nombrecliente = input(" ingrese su nombre: ")
    dicccliente[idcliente] = nombrecliente


def opciones():
    print("\n")
    msg = "Gestor de Clientes"
    print(msg)
    print (" * " * len(msg))
    opcmen = {1: "registrar cliente", 2: "Listar Clientes", 3: "Buscar Clientes", 4: "Salir"}
    for op, opm in opcmen.items():
        print("{}. {}".format(op, opm))

def menu():
    op = 0

    while op != 4:
        opciones()
        op = int(input("indique su opcion [1...4] --> "))
        if op in range (1,5):
            if op == 1:
                registrarcliente()
            elif op == 2:
                 listarcliente()
            elif op == 3:
                 buscarcliente()
            else:
                print ("... bye")
        else:
            print("opcion no valida, elija otra opcion, por favor.")

menu()
