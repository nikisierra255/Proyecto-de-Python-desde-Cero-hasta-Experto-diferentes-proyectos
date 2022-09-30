#ejercicio 1 cadena mas larga

# cadena mas larga en una oracion o frase


cadena = "Maria tenia un corderito llamado pepe"

listapal = cadena.split(" ")

maslarga = ""

for pal in listapal:
    if len (pal) > len(maslarga):
        maslarga = pal
print (maslarga)

