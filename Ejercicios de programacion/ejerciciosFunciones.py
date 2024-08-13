"""
Ejerricio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial
"""


def ejercicio3():
    numero = int(input("Ingrese el numero: "))
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(factorial)


"""
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad 
sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el 
porcentaje de IVA, deberá aplicar un 21%
"""


def ejercicio4(cantidad, iva=21):
    iva = iva / 100
    precioConIva = cantidad * (iva + 1)
    print(precioConIva)


"""
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un 
cilindro usando la primera función.
"""


def areaCirculo(radio):
    area = 3.1416 * (radio ** 2)
    return area


def ejercicio5(altura):
    area = areaCirculo(32)
    print(area)
    volumen = area * altura
    print(volumen)


"""
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""

lista = [2, 54, 8, 6, 2, 86, 243, 768, 987, 24, 109, 86, 213, 6475, 87665, 432, 678, 78]


def ejercicio6(numeros):
    suma = 0
    for i in numeros:
        suma += i
    media = suma / len(numeros)
    #print(media)
    return media


"""
Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""


def ejercicio7(numeros):
    cuadrados = []
    for i in numeros:
        cuadrados.append(i ** 2)
    print(cuadrados)


"""
Ejercicio 8
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
varianza y desviación típica.
"""


def ejercicio8(numeros):
    media = ejercicio6(numeros)
    sumatoria = 0
    for numero in numeros:
        sumatoria += (int(numero) - media) ** 2
    varianza = (sumatoria / len(numeros))
    desviasion_tipica = (sumatoria / len(numeros)) ** 0.5
    print(f"Media = {media}, Varianza = {varianza}, Desviasion tipica {desviasion_tipica}")


"""
Ejercicio 9 *****
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""


def maxcd(a, b):
    while b != 0:
        x = b
        b = a % b
        a = x
    return a


def mincd(a, b):
    mcd = a * b / maxcd(a, b)
    return mcd


#print(maxcd(23, 54))
#print(mincd(23, 43))
"""
Ejercicio 10 ***
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
"""


def decimalBinario(numero):
    numeroBinario = ""
    while numero:
        numeroBinario += str(numero % 2)
        numero = (numero // 2)

    return numeroBinario[::-1]


def binarioDecimal(numero):
    numeroDecimal = 0
    num = numero
    temp = num
    base = 1
    while temp:
        siguiente = temp % 10
        temp = temp // 10
        numeroDecimal += siguiente * base
        base = base * 2
    return numeroDecimal


#print(decimalBinario(11))
#print(binarioDecimal(1011))
"""
Ejercicio 11
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su 
frecuencia. 
Escribir otra función que reciba el diccionario y devuelva una tupla con la palabra más repetida y su frecuencia.
"""

frase = ("Pero ahora vienes a mí a decir Don Corleone pido justicia y pides sin ningún respeto no como un amigo ni "
         "siquiera me llamas Padrino")


def cuentaFrecuencia(frase_i):
    diccionario = {}
    fraseDividida = frase_i.split(" ")
    for i in fraseDividida:
        contador = fraseDividida.count(i)
        diccionario[i] = contador
    return diccionario


def geneaDiccionario(dic):
    #Esta forma aplica si solo hay UN SOLO valor mas grande
    elemento = []
    for key, values in dic.items():
        if values > 1:
            elemento.append((key, values))
    masGrande = tuple(elemento[0])
    #Otra forma es:
    palabra = " "
    frecuencia = 0
    for k, v in dic.items():
        if v > frecuencia:
            palabra = k
            frecuencia = v
    return palabra, frecuencia


print(geneaDiccionario(cuentaFrecuencia(frase)))
