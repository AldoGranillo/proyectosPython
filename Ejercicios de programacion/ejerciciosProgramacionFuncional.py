import math

"""
Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una
de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la
cesta y devolver el precio final de la cesta.
"""


def descuento(precio, valor):
    #Como no indica el descuento aplicaremos del 50%
    precioDescuento = precio * (valor / 100)
    return precioDescuento


def iva(precio, precioIva):
    precioIva = precioIva / 100
    precioConIva = precio * (precioIva + 1)
    return precioConIva


def canasta(dicc, funcion):
    total = 0
    for precio, des in dicc.items():
        total += funcion(precio, des)
    return total


#print(canasta({1000: 20, 500: 10, 100: 1}, descuento))
#print(canasta({1000: 20, 500: 10, 100: 1}, iva))

"""
Ejercicio 2
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial 
y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una 
tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""


def calculadora():
    print("Bienvenido ingrese la funcion que quiere calcular: \n(1) Seno \n(2) Coseno \n(3) Tangente \n(4) Exponencial "
          "\n(5) Logaritmo neperniano")
    opcion = int(input(": "))
    valor = int(input("Ingrese el numero a calcular: "))
    if opcion == 1:
        valores = []
        for i in range(1, valor):
            valores.append((i, math.sin(i)))
        return valores
    elif opcion == 2:
        valores = []
        for i in range(1, valor):
            valores.append((i, math.cos(i)))
        return valores
    elif opcion == 3:
        valores = []
        for i in range(1, valor):
            valores.append((i, math.tan(i)))
        return valores
    elif opcion == 4:
        valores = []
        for i in range(1, valor):
            valores.append((i, math.exp(i)))
        return valores
    elif opcion == 5:
        valores = []
        for i in range(1, valor):
            valores.append((i, math.log(i)))
        return valores
    else:
        print("Valor invalido")
        pass


"""
Ejercicio 3
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la 
función dada a cada uno de los elementos de la lista.
"""


def cuadrado(lista):
    cuadrados = []
    for i in lista:
        cuadrados.append(i ** 2)
    return cuadrados


def funcionxd(lista, funcion):
    return funcion(lista)


#print(funcionxd([100, 24, 4, 78, 89, 87, 43, 1, 78, 9, 2], cuadrado))
"""
Ejercicio 4
Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista 
que devuelvan True al aplicarles la función booleana.
"""


def funcionBoleana(lista):
    listaTrue = []
    for i in lista:
        if i % 3 == 0:
            listaTrue.append(i)
    return listaTrue


def principal(lista, funcion):
    return funcion(lista)


#print(principal([100, 24, 4, 78, 89, 87, 43, 1, 78, 9, 2], funcionBoleana))
"""
Ejercicio 5
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
"""

frase = ("Pero ahora vienes a mí a decir Don Corleone pido justicia y pides sin ningún respeto no como un amigo ni "
         "siquiera me llamas Padrino")


def ejercicio5(cadena):
    alamcen = {}
    for i in cadena.split():
        alamcen[i] = len(i)
    print(alamcen)


"""
Ejercicio 6
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""


def ejercicio6(notas):
    evaluacion = []
    for i in notas:
        if i >= 6:
            evaluacion.append((i, "Aprobado"))
        else:
            evaluacion.append((i, "Suspendido"))
    return evaluacion


#print(ejercicio6([6, 4, 8, 10, 2, 5, 7, 7, 8, 9, 10]))
"""
Ejercicio 7
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario 
con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
"""


def ejercicio7(diccionario):
    notasMayuscula = {}
    for key, value in diccionario.items():
        if value >= 6:
            notasMayuscula[key.upper()] = 'Aprobado'
        else:
            notasMayuscula[key.upper()] = 'Reprobado'

    return notasMayuscula


#print(ejercicio7({'matematicas': 7, 'español': 8, 'ciencias naturales': 9, 'historia': 5}))
"""
Ejercicio 9
Escribir una función que calcule el módulo de un vector.
"""


def ejercicio9(x, y):
    modulo = ((x ** 2) + (y ** 2)) ** 0.5
    return modulo


#print(ejercicio9(4, 7))
"""
Ejercicio 10
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio
sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada 
diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en 
función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
"""

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
             {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
             {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
             {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
             {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def ejercicio10(lista, valor):
    listaNueva = []
    for i in range(len(lista)):
        metros = lista[i].get('metros')
        habitaciones = lista[i].get('habitaciones')
        garaje = int(lista[i].get('garaje'))
        anos = lista[i].get('año')

        if lista[i].get('zona') == 'A':
            lista[i]['precio'] = ((metros * 1000) + (habitaciones * 5000) + (garaje * 15000)) * (
                    1 - (2020 - anos) / 100)
        else:
            lista[i]['precio'] = ((metros * 1000) + (habitaciones * 5000) + (garaje * 15000)) * (
                    1 - (2020 - anos) / 100) * 1.5

        if lista[i].get('precio') <= valor:
            listaNueva.append(lista[i])
        else:
            pass
    print(listaNueva)


"""
Ejercicio 11
Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya 
puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando el valor 
menos la media y dividiendolo por la desviación típica de la muestra.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]


def ejercicio11(muestra):
    media = sum(muestra) // len(muestra)
    varianza = sum((x - media) ** 2 for x in muestra) / len(muestra)
    desviacionTipica = math.sqrt(varianza)
    puntuacionTipica = []
    for i in muestra:
        puntuacion = (i - media) / desviacionTipica
        if puntuacion > 3 or puntuacion < -3:
            puntuacionTipica.append(i)

    return puntuacionTipica


print(ejercicio11(numeros))
