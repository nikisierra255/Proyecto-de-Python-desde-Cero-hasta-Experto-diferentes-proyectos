#colecciones - conjuntos

# los conjuntos en la lista a imprimir eliminan automaticamente los numeros
#repetidos en la tuplas o lista#

conjunto = {1,1,2,3,3,4,5}
print (conjunto)


#no es un conjunto, mas bien tomaria el nombre de libreria vacia

x ={}
print(x)

z = {True, "hola", False, "mundo", 1,4.0,4,0}
print (z)


#conjunto clase set (este se encarga de elimiar los elementos de una lista o tupla repetidos)
# y ordenado de menor a mayor


conjunto_set = set([10,10,22,22,31,31,4,5])
print(conjunto_set)




#conjunto frozentset elimiana los duplicados y los imprime ordenado de menor a mayor.
#con la clase set
conjunto_Fro = frozenset ([10,10,22,22,31,31,4,5])
print(conjunto_Fro)



#una variable declarada con la clase set, vacia, imprime nada
s_x = set ()
print(s_x)


#estas declaraciones se utilizan para recorrer un conjunto atraves de un ciclo
#FOR IN

my_set = {1,1,2,3,7,3,2}
for s in my_set:
 print(s)



#como saber si un elemento esta en el conjunto, se utiliza la Ddeclaracion (in)

print( 2 in my_set)


#longitud del conjunto se obtienen declarando con la variable (len)

print(len(my_set))






#operaciones con conjutos
#metodo creacion del conjunto: my_set

my_set ={1,3,7,9,11}
print(my_set)


#metodo añadiendo un elemento al conjunto
my_set.add(4)
print(my_set)




#metodo añadiendo una lista de elementos al conjunto
my_set.update([1,3,2,6,8])
print(my_set)


#metodo eliminar elementos en un conjunto

my_set.remove(3)
print(my_set)




#metodo set.pop elimina un elemento aleatorio de la lista de conjunto.

my_set.pop()
print(my_set)




#metodo set.discard elimina un elemento  de la lista de conjunto indicado, si el elemento no esta en la lista no hace nada.

my_set.discard(9)
print(my_set)




#metodo set.clear elimina todos los elementos de una lista, dejando la lista vacia, estos metodos son para lista mutable
my_set.clear()
print(my_set)



# metodos y operaciones sobre conjuntos

#la union de los conjuntos, se puede realizar atraves del metodo unión.

a={1,2,3,4}
b={4,5,6,7}
print (a.union(b))



# para el metodo union tambien se puede utilizar (|) (alt+124)

print (a|b)




# el metodo para intersencion de conjunto se realiza con a.intersection o &
print (a.intersection(b))

print (a&b)



#la diferencia de conjunto se puede realizar con el metodo (difference) o (-)

print (a.difference(b))

print (a-b)



#para la diferencia simetrica existe el metodo (a.symmetric_difference).
#tambien se puede realizar la diferencia simetrica con a ^ b.

print (a.symmetric_difference (b))

print (a^b)


#superconjunto puede emplearse el metodo (issuperset) este
#recibe un conjuto como parametro o el operador mayor o igual a
#en cualquier de los dos casos, se recibe un valor falso o verdad.

print (a.issuperset (b))

print (a >= b)

#subconjunto pueden emplearse en metodos (issubset) este
#recibe un conjuto como parametro o el operador menor o igual a
#en cualquier de los dos casos, se recibe un valor falso o verdad.

print (a.issubset(b))

print (a<b)


#disjuntos se puede enplear el metodo (isdisjoint) este
#recibe un conjuto como parametro y devuelve el valor True sino hay elementos comunes entre los conjutos.
print (a.isdisjoint(b))