#####estrutura de control (break y continue):
####
####la instruccion break corta ejecuccion de una estrutura iterativa de acuerdo a
####una condicción dada.
##
#### ejemplo:

i = 0
while True:
    if i > 100:
        break
    print(i)
    i=i+1

#### instruccion break en For.
###ejemplo:

##coleccion = [2,4,5,7,8,9,3,4]
##for num in coleccion:
##    if num == 7:
##        break
##    print(num)

#### instruccion continue en while
##
###ejemplo

##var = 10
##while var == 10:
##    var = var - 1
##    if var == 5:
##         continue
##    print ("valor actual de var:" + str (var))


#instruccion continue en For
 #ejemplo

##coleccion =[2,4,5,7,8,9,3,4]
##for num in coleccion:
##    if num % 2  != 0:
##        continue
##    print (num)

