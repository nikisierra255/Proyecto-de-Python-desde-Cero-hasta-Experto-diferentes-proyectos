#tupla con una lista normal.
tupla = (2555,"niki",18.6,16)
print (tupla)





#otra forma de hacer una tupla
tupla2 = 1,2,3
print(tupla2)





#tupla vacia
tuVac = ()
print (tuVac)





#tupla unitaria

tuplaUni = (45,)
print (tuplaUni)






#imprimir uno por uno el detalle los elementos en una tupla
print (tupla [0])
print (tupla [1])
print (tupla [2])
print (tupla [3])






#imprimir uno por uno el detalle los elementos en una tupla desde atras hacia adelante
#poniendo numero negativos

print (tupla [-1])
print (tupla [-2])
print (tupla [-3])
print (tupla [-4])





# para imprimir el tamaño de una tupla
print (len(tupla))



#recorrido en una tupla
for t in tupla:
    print(t)






#operaciones con tuplas
#slicing (rebanado)
tupla1 = ("a","b","c","d","e","f")
print (tupla1[0:3])



# asignarle un slicing (rebanado) dentro de una tupla a una variable ejemplo
tupla1 = ("a","b","c","d","e","f")
t = tupla1[0:3]
p = tupla1[2:5]
print (p)




#operaciones con tuplas (concatenacion (+) de tuplas) unir 1 o mas tuplas.
a = (1,2,3)
b = (4,5,6)
c = a+b
print (c)




# metodos de tuplas (metodo count (elemento))
t1 = (1,3,2,5,6,2)
print (t1.count(5))



#metodos de tuplas (metodo index (elemento, [indiceInic],[indiceFin]))

t1 = (1,3,2,5,6,2)
print(t1.index(2,3,6))




#tuplas y funciones

#funcion (LEN) (dice cuantos elementos tiene la tupla o lista)
t = (5,2,0,8,-2)

print(len(t))




#funcion (MAX) (dice cual numero es mayor dentro de la tupla o lista)
t = (5,2,0,8,-2)

print(max(t))


#funcion (MIN) (dice cual es el elemento menor en la tupla o lista)

t = (5,2,0,8,-2)
print(min(t))



#funcion (SUM) (devuelve la sumatoria de todos los elementos numericos de una tupla o lista *solo numero)

t = (5,2,0,8,-2)
print(sum(t))