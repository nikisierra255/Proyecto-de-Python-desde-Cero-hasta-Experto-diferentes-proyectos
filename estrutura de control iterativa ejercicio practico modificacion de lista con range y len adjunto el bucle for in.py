##estrutura de control iterativa ejercicio practico
##modificar los elementos de una lista (bucles)

# modificar elementos de una lista

lista = [30,50,21,-39,0,36,+6]
i = 0
for x in lista:
    lista[i] = x + 1
    i = i+1
print(lista)


## ejemplo de lista con cadena

listac = ["kmik","njnjnj","ujjnjnj","njnjhb","gvgvg"]
i = 0
for x in listac:
    listac[i] = x + "-p"
    i = i+1
print(listac)

#el fragmento de codigo debajo se utiliza para modificar la lista usando los parametros del range y len
for i in range (0,len (listac), 2):
    listac[i] = "python"
print(listac)