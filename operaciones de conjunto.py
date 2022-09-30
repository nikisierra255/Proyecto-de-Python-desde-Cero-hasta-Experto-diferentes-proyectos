##ejercicio 2
##operaciones de conjuntos con lista

a = [1,2,4]
b = [1,2,3,5]

##union -> conjunto con los elementosss del conjunto a y del conjunto b sin elementos repetidos
aub = list(a)
for ele in b:
    if not ele in  aub:
        aub.append(ele)
print("union- >", sorted(aub))

##interseccion -> conjunto con los elemntos comunes en ambos conjuntos

ainterb = []
for ele in b:
    if  ele in a:
        ainterb.append(ele)
print("interseccion- >", sorted(ainterb))


##diferencia -> a - b, conjunto con los elemntos de a que no esten en b

adifb = list(a)
for ele in b:
    if  ele in adifb:
        adifb.remove(ele)
print("diferencia - > ", sorted(adifb))


##diferencia simetrica -> conjunto con elemntos de a que no esten en b y viceversa

adifsb = list()
for ele in a:
    if  not ele in b:
        adifsb.append(ele)

for ele in b:
    if  not ele in a:
        adifsb.append(ele)

print("diferencia simetrica- > ", sorted(adifsb))


##super conjunto -> se verifica si a contiene a b

super = True
for ele in b:
    if  not ele  in a:
        super = False
        break
if super:
    print ("super conjuto")
else:
    print ("no es super conjunto")

##subconjunto -> se verifica si a contiene en b

sub = True
for ele in a:
    if  not ele  in b:
        sub = False
        break
if sub:
    print ("subconjuto")
else:
    print ("no es subconjunto")


##disjuntos -> se verifica que los elementos de ambos conjuntos sean diferentes


disj = True

for ele in a:
    if   ele  in b:
        disj = False
        break
if disj:
    print ("disjuntos")
else:
    print ("no es disjuntos")