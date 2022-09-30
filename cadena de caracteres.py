### cadena de caracteres- declaraciones
##son secuencia inmutable que contienen caracteres unicode



             #SINTAXIS
id_variable = "conjunto de caracteres"  #(se pueden encerrar en comillas dobles)

linea = "programacion ejemplo"

id_variable = 'conjunto de caracteres' #(tambien se pueden encerrar entre comillas simples)

area = 'computacion ejemplo'

#Tambien se pueden encerrar entre triple comillas, ya sean dobles o simpres, para una
#cadena de multiples lineas


                                   #sintaxis
id_variable = """ conjunto
                       de
                         caracteres"""
titulo = """ fundamentos
                      de programacion
                       en python"""


                      #cadenaas - caracteres de escape
text = "Que bonito es \"programar\""
print (text)



# \n salto de linea o linea nueva

esc = 'programando \n en \n \'python\''
print(esc)




# \t tabulador

#agrega espacio amplio entres carateres

esc = "programando \t en\t \'python\'"
print (esc)


#\' insertar comillas simples entre los caracteres

esc = "programando \n en \n \'python'"
print(esc)


# \" insertar comillas cobles entre los carecteres
print ("la \" vida \" es lo mas valioso que tenemos")




#aqui, \n es interpretado como nueva linea
s = 'C: \python\n noticias'
print(s)

#en una raw string <-- (cadena cruda) no se interpreta el caracter \

s = r'C:_\python\noticia'
print(s)




#operaciones con cadena
#1 . - acceso a caracteres especificos de la cadena a traves de [], desde la posicion 0.

x = "programando en python"
x = [6]

print ("x[0]=", x [0])





#concatenacion de cadena

##2-. concatenar 2 o mas cadenas, a traves de :
##    * operador +
##    * dos cadenas escritas una al lado de la otra o con ()

cad1 = " programando en ... "
cad2 = "python"
cadR = cad1 + cad2
print (cadR)

cadRP = ("progranado en ... python")
cadRP1 = ("3")

print( cadRP + cadRP1 )



##3.- comprobrando existencia de sub-cadena en una cadena a traves de in.

print ("a" in cadRP)

print("bn" in cadRP)

print("hhon" in cadRP)



## repetir unacadena usasando el operador (*)

cad1 = "programando en"
cad2 =  "...python"
cadR = (cad1+cad2 * 3)
print (cadR)





#funciones en cadenas

##1.- len(): funciona para devolver la longitud de una cadena determinada

cad1 = " progrando en "
cad2 = "...python"
cadR = ( cad1 + cad2 * 3)
print (cadR)

print (len(cadR))



#2.- str() convierte el argumento dado en cadena.

cad1 = " progrando en "
cad2 = "...python"
cadR = ( cad1 + cad2 * 3)
print (cadR)

print (len(cadR))
print (str(len(cadR)))
