#METODOS

#metodo get (), este recibe una clave y un valor por defecto
#si la clave aparece en el diccionario, (get) devuelve el valor correspondiente
#en caso contrario, devuelve el valor por defecto.

# ejemplo

diccionario = {1: "a", 2: "b"}
print (diccionario.get (3,0))

print (diccionario.get(2,0))


# metodo (setdefault) este metodo permite agregar elementos en diccionarios
#recibe una clave y el valor, si la clave existe, devuelve el valor
# de la clave.

diccionario.setdefault (3,[3,3])
print (diccionario)


#metodo (update), devuelve el diccionario actualizado, apartir de otro diccionario
#recibe como parametro otro diccionario #si se tienen claves iguales, actualiza clave repetida
#si no hay claves iguales, este par de clave / valores es agregado al diccionario.

diccionario = {1: "a", 15: "T", 10: "r"}
diccionario2 = {4:"s",8:"f"}
diccionario.update(diccionario2)
print (diccionario)



#metodo (values) devuelve una lista con los valores del diccionario
print (diccionario.values())



# metodo (items)devuelve una lista de tupla, cada tupla con el par clave/valor

print (diccionario.items())


#metodo (keys) este devuelve una tupla con las claves del diccionario

print (diccionario.keys())



#metodo (copy), devuelve una copia originar de la tupla original
diccionario2 = diccionario.copy()
print (diccionario)
print (diccionario2)





#metodo (CLEAR) elimina todos los item de la lista

diccionario2.clear()
print(diccionario2)
#para confirmar su eliminacion, hacemos un print a la misma tupla limpiada.
#y podremos darnos cuenta de que ya no existen sus items
print (diccionario2)





#metodo (pop) puede ser utilizado para borrar o eliminar elementos de un
#diccionario, recibe como elemento una clave o el elemento eliminado.

print (diccionario)

print (diccionario.pop(10))

print (diccionario)






          #funciones en diccionario#

#funcion sorted (id_diccionario), sive para obtener una lista ordenada de clave
#contenida en el diccionario de menor a mayor.

diccionario3 = {430: "matematica", 215: "fisica", 324: "quimica", 123: "Literatura"}
print (sorted(diccionario3))



#funcion (len(id_diccionario)/(len) devuelve el numero total de pareja
#clave/valor contenida en el diccionario.

print (len(diccionario))






#funcion (del(id_diccionario[clave]))  elimina un par clave/valor de un diccionario
#recibe un diccionario como parametro.

del(diccionario[8])
print (diccionario)



#funcion (list) con esta funcion se puede obtener una lista de las siguientes funciones

#para llamr una lista con list y el metodo keys
print (list(diccionario.keys()))

#para llamar una lita con list y el metodo values
print (list(diccionario.values()))

#para llamar un lisa con list y el metodo items
print (list(diccionario.items()))





