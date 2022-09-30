 #crear agenda con diccionario

agenda = {}

cantidad = int(input("indique la cantidad a agendar: "))
if cantidad > 0:
    print (" --- AGENDA--- ")
    for c in range(0, cantidad):
        nombre = input("nombre de contacto: ")
        if nombre in agenda:
            print ("{} ya registrado, su numero {}" . format(nombre,agenda[nombre]))
        else:
                agenda[nombre]=input("indique el numero de telefono: ")
    print("\Listado de contactos")
    for nombre , numero in agenda.items():
        print(nombre, "-->", numero)
else:
    print("la cantidad de contactos debe de ser positiva")