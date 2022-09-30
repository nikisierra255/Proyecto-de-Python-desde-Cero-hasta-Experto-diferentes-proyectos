#metodos de cadenas


#sintaxis para el uso de los metodos

##id_variable_cadena.nombre_metodo()

#metodo capitalize() retorna una cadena con la primera letra en mayuscula

cadena = "programando en python"
print(cadena.capitalize())

#-----------------------------------------------------------------------------


#metodo count (subcadena[, inicio[, final]]), retorna un entero indicando
#la cantidad de apariciones de la subcadena, dentro de la cadena.

cadena = "programando en python" .capitalize()
print(cadena.count("o"))



#--------------------------------------------------------------------------


#metodo find (subcadena[, inicio[, final]]) retorna un entero, representando la
#la posicion donde inicia la subcadena, dentro de la cadena, si no la encuentra
#retorna -1


cadena = "porgramando en python" .capitalize()
print(cadena.find("en"))



print (cadena.find("en",0,11))
###-----------------------------------------------------------------------------
##
###metodo format (*argumento, **kwargs) devuelve una copia de la cadena donde cada
###campo de rempleza o posicion indicado por la llave, se sustituye, con el valor del arismento correspondiente
###el posicionamiento o reemplazao en la cadena se pueden dar de la siguientes maneras, los argumentos
###se posicionan en la cadena mediante un numero entre las llaves {}, cuando las llaves {}, estan vacias
###la ubicacion de los argumentos es por defecto, tambien podemos tener identificadores de variables entre las llaves {}
###que corresponderan con los identificadores de variable de mlos argumentos


print ("la suma de {0} + {1} es {2} ".format(1,2,1 + 2))


print ("{2} se genera de {0} + {1}".format (1,2,1 + 2 ))


print("las frutas mas sabrosaas son las {} y las {}".format("fresas","manzanas")) #aunque los corchetes esten vacios, por defecto se imprime en orden en pantalla.


print("las frutas mas sabrosas son {f2} y las {f1}".format (f1 = "fresa", f2 = "manzanas"))  #con identificadores en los corchetes.


###-----------------------------------------------------------------------------------------
##
###metodo index (subcadena [, inicio[,final]]) retorna una entero que representa la posicion donde inicaq la sub cadena
###dentro de la cadena. el inicio y el final son opcionales, si la subcadena no se encuenta en la cadena, genera un error de valor.

cadena = "programando en python".capitalize()
print(cadena.index("en"))

# si el valor no esta en la subcadena, arroja un error valueError
# print (cadena.index("en" , 0 ,11))




###----------------------------------------------------------------------------------
##
#####metodo replace (sub a reemplazar, sub nueva), recibe los argumentos a reemplazar y la sub cadena nueva,
####retorna la cadena con la sub cadena reemplazada

cadena = "programando en visual"
print (cadena.replace("visual" , "python"))


###METODO SPLIT ("SEPARADOR) retorna
####lista con todos los elemetos encontrados al dividir la cadena con un separador
###recibe un argumento separador.

groupwords = "programando con python"
print (groupwords.split(" "))


#-----------------------------------------------------
##metodo join(iterable) retorna la cadena formada por los elementos del iterable
##unidos a la cadena, la cadena es concatenada, a cada uno de los elementos del iterable
##excetuando el ultimo elemento.


formato_numero_factura = "N° 0000-0", -0000 ("ID:","")
numero  = "275"
numero_factura = numero.join (formato_numero_factura)
print (numero_factura)


#---------------------------------------------------------------
##metodo lower() retorna una copia de la cadena en minuscula

cadena = "PROGRAMANDO EN PYTHON"
print (cadena.lower())



#----------------------------------------------------------
#metodo upper, devuelve una copia de la cadena en mayuscula

cadena = "programando en python"
print(cadena.upper())




#-------------------------------------------------------------
#metodo partition ("separador")

##divide la cadena en la primera aparicion del separador y devuelve una tupla de 3
##que contiene la parte antes del separador, el separador en si y la la parte despues del separador, si no se encuentra el separador
##devuelve una tupla de 3, que contiene la cadena en si, seguida de 2 cadena vacia, recibe un argumento separador

url = "http: //www.g-talent.net"
print (url.partition ("www."))


protocol, separador, domain = url.partition("www.")
print("protocolo:{0}\n dominio: {1}".format(protocol,domain))
