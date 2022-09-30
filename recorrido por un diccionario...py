

                     #colecciones - diccionario#
                     #recorrido de diccionario#

#-------------------------------------------------------------------------------
#recorrido por clave
# for <clave> in <diccionario>:
    #accion 1
    #*******
    #accion 2
#-------------------------------------------------------------------------------
dicc = {1: "mat", 2:"fis", 3:"lit"}
for clave in dicc:
    print (clave,dicc[clave])



#-------------------------------------------------------------------------------
#recorrido por valor
# for <valor> in <diccionario>.items():
    #accion 1
    #*******
    #accion 2
#-------------------------------------------------------------------------------

for valor in dicc.items():
    print (valor)






#-------------------------------------------------------------------------------
#recorrido por clave - valor
# for <clave> , <valor> in <diccionario>.items():
    #accion 1
    #*******
    #accion 2
#-------------------------------------------------------------------------------

for clave,valor in dicc.items():
    print(clave, valor)