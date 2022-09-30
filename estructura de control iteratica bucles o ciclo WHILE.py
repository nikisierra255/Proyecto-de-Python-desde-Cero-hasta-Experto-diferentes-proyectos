####estructura de control iterativa (bucles o ciclos (bucles while))
####definicion: bucles o ciclos, se emplean cuando se quiere que una o mas intrucciones
####se repitan cierta cantidad de veces, el bucle while (mientras) trabaja de la siguiente manera
####
####1: se evalua una condicion
####2: si es verdadera
####3: se ejecuntan una o mas intruciones (y se vuelve a evaluar la condicion, si sigue siendo verdadera)
####4: cuando la condicion deje ser verdadera osea (falsa), automaticamente el ciclo termina
##
##
##
###suma de cuadrado de los n primeros numeros.
##n = int(input("ingrese la cantidad de nuemros: "))
##s = 0
##i = 1
##while i <= n:
##      c=i**2
##      s+=c
##      i+=1    #contador
##print ("la suma es: ",s)
##
##
###ejemplo de bucles while con (edad+1)
##
##edad = 0
##while edad < 18:
##    edad = edad + 1
##    print ("felicitaciiones, tiene: ", edad )


#ejemplo calcula el promedio de nota de una curso

promedio, total, contar = 0.0,0,0
sigo = True
while sigo:
        notadef = float(input("introduzca la nota de un estudiante: "))
        total= total+ notadef
        contar = contar + 1
        print ("procesar otro estudiante: (s-si, n-no): ")
        respuesta = input()
        if respuesta == "n": sigo = False
promedio = total/contar
print("promedio de notas del curso es: " + str(promedio))
