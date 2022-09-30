# Control de estrutura iterativa
# tabla de multiplicar con bucles con for (anidadas) in range

print( " Tabla de multiplicar " )
for x in range (1,10):
    print( "tabla del " , x )
    for y in range (1,11):
        print(x, "*" , y , " = " , x * y )
    print()

    #los for que estan uno dentro de otros es una estrutura anidada
    #con la funcion range