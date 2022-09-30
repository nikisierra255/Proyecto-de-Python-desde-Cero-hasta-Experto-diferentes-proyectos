#####cadenas de caracteres- recorrido
####
####cara caracter ocupa una longitu desde la posicion 0 hast la posicion -1
####
#### p y t h o n
#### 0 1 2 3 4 5
####
####en python se pueden recorrer una cadena de diferentes maneras unas de ellas es
###con el ciclo for in:
##
##cadena = "correa"
##for c in cadena:
##    print(c)
##
###--------------------------------------------------------------------------
###recorrer una cadena con la sentencia len
##i = 0
##cadenaa = "cadena"
##while i < (len(cadenaa)):
##    print(i, cadenaa[i])
##    i=i+1
###-------------------------------------------------------------------------
###recorrer una cadena con la sentencia (for) , (in), (range) + (len)
##
##cadete = "cadena"
##for i in range(len(cadete)):
##    print(i,cadete[i])
###-----------------------------------------------------------------------
##
###otra forma de recorrer una cadena es con la sentencia (enumerate)
##
##cadena = "nikito es el mejor"
##for pos in enumerate (cadena):
##  print(pos)
##
##
###----------------------------------------------------------------------
##
###una variante a la manera anterior es:
##
##cadena = "nikito es el mejor"
##for i, c in enumerate (cadena):
##  print(i , cadena[i])
##
###---------------------------------------------------------------------
##
##                         #slicing (rebanado)#
##
####sintaxis
####secuencia [inicio:fin]
####
####ejemplo


cadenaaa = "programando en python con g-talent"

print(cadenaaa [ 0: 11 ])


cadenaaa = "programando en python con g-talent"

print(cadenaaa[ : 11 ])

cadenaaa = "programando en python con g-talent"

print(cadenaaa[ 15 : 21 ])


arana = "programando en python con P-niki sierra"
print (arana [arana.index("P"):])



###slicing con indice negativo

cadenaaa = "programando en python con g-talent"

print(cadenaaa[: - 1])


#----------------------------------------------------------------------
cadenaaa = "programando en python con g-talent"
print(cadenaaa [-30: 26])

#---------------------------------------------------------------------------

cadenaaa = "programando en python con g-talent"

print(cadenaaa[-20:-1])
#------------------------------------------------------------------------
niki = "programando en python con g-talent"
print (niki [ -34:])


#---------------------------------------------------------------------------------



#slicing paso a paso

#secuencia [inicio:fin:paso]


nikito = "programando en python con g-talent"
print (nikito[::2])


#------------------------------------------------------------------------------
nikito = "programando en python con g-talent"
print(nikito[15::3])



#--------------------------------------------------------------------------
nikito = "programando en python con g-talent"
print(nikito[15::-3])



#lo aprendido hoy, manipulacion de indice para acesar a los carateres de las cadenas
#y slicing(rebanado)