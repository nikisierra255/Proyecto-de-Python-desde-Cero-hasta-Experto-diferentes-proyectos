# DIBUJAR UN RECANGULO

def esp_ast (nspace, nasterisco):
    print(nspace *" ", nasterisco *" *")

def rectangulo(base, altura):
    for x in range (0, altura):
        esp_ast(base+altura, base)

def principal():
    base = int(input(" indique la base del rectangulo: "))
    altura = int(input(" indique la altura del rectangulo: "))
    print()
    if base > 0 and altura > 0 and base != altura:
        rectangulo (base,altura)
    else:
        if base == altura:
            print("la base y la altura deben de ser diferentes ")
        else:
            print("la base y la altura deben de ser positivas ")
principal()