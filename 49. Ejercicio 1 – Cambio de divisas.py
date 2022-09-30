
# cambio de divisa

# ejercicio cambio de divisas

# datos de entrada:
    # tipo de moneda que tienes -PC   USA EU
    # Monto a cambiar
    # Tipo de moneda que deseas - USA, EU


# Proceso:
    # cambio = monto_monda_tiene / valor_moneda_cambio
    # dolar = {"PC": 3844.05, "EU" : 0.53323}
    # euro ={"PC" : 4900.09, "USA" : 1.17186}

#Salida:

# Imprimir el montot obenido en el cambio y la moneda
def PC (*Change):
    Pesos_colombiano ={"USA" : 1.17186, "EU" : 0.53323}
    return Change[1]/PC[Change[0].upper()]

def EU(*Change):
    euro ={"PC" : 4900.09, "USA" : 1.17186}
    return Change[1]/euro[Change[0].upper()]

def USA (*Change):
    dolar = {"PC": 3844.05, "EU" : 0.53323}
    return Change[1]/dolar[Change[0].upper()]

def Captura_datos():
    monedatiene = input("cual moneda tienes?   ---> PC - pesos col. , USA - Dolares Americanos. , EU - Euros: ")
    montocambiar = float(input("indique el monto a cambiar: "))
    monedacambiar = input ("moneda a cambiar -> USA , EU, PC : ")
    return monedatiene, montocambiar, monedacambiar

def imprime(montocambiado, monedacambio):
    print("su cambio es: ", format(montocambiado), monedacambio)

def cambio():
    datos = Captura_datos()
    if datos [2].upper() == "USA":
        montocambiado = USA(datos[0], datos[1])
    else:
        montocambiado = EU(datos[0], datos[1])
    imprime (montocambiado, datos[2])

cambio()