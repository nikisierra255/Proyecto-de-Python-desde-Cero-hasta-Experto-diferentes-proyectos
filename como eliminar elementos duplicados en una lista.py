#Eliminar elementos duplicados de una lista

lista = [5,5,5,7,8,8,8,9,12,12,12,5,5,9,9,4,4,1,1]

nueva = []
for ele in lista:
   if not ele in nueva:
         nueva.append(ele)
print (nueva)

# otra forma

lnew = set(lista)
lnew =list(lnew)
print(lnew)

#otra forma

lnew = list(set(lista))
print(lnew)