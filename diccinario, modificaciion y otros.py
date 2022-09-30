diccionario = dict (a = 1,b = 2,c = 3)

diccionario = dict ()
diccionario ["nombre"] = "pepe"
print (diccionario)

#insersion de valores, si hay valor predeterminado en una clave
#y usted ingresa otro valor en esa clave, lo que hara
#python, es ingresar el valor en la clave modificando en anterior al que estaba.

diccionario = dict (a=15,b = 0, c = -20)

diccionario ["b"] = 30
print (diccionario)


#modificacion de valores en diccionario

diccionario =  dict(a=15,b = 0, c = -20)

diccionario ["b"] = 30
diccionario ["c"] = 0
print (diccionario)

diccionario ["a"] = [123,"ABC"]
print (diccionario)







#detectando clave en diccionario con el rango (IN)

print ("t" in diccionario)

print ("a" in diccionario)