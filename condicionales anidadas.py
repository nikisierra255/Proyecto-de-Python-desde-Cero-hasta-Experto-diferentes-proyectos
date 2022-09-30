y = 88
#si (if) y es mayor 0
if y > 0:
    #si(if) y se encuentra en un rango
     if y in range (1,100):
         print ("dentro del rango")
     else:
         print ("fuera del rango")

    #de lo contrario si (if) y es menor a 0
elif y < 0:
    print ("numero negativo")
    #en caso contrario
else:
    print ("numero neutro cero")
