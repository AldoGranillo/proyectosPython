"""
EJERCICIO 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""


def ejercicio1():
    palabra = input("Ingrese una palabra: ")
    for i in range(10):
        print(palabra)


"""
EJERCICIO 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
que ha cumplido (desde 1 hasta su edad).
"""


def ejercicio2():
    edad = int(input("Ingrese su edad: "))
    for i in range(edad):
        print(f"Haz cumplido {i + 1} años")


"""
EJERCICIO 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas.
"""


def ejercicio3():
    numero = int(input("Ingrese un numero entero: "))
    for i in range(numero + 1):
        if i % 2 != 0:
            print(i, end=",")


"""
EJERCICIO 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta 
atrás desde ese número hasta cero separados por comas.
"""


def ejercicio4():
    numero = int(input("Ingrese un numero: "))
    while numero > -1:
        print(numero, end=",")
        numero -= 1


"""
EJERCICIO 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""


def ejercicio5():
    cantidad = int(input("Ingrese una cantidad a invertir: "))
    interes = int(input("Ingrese el interes anual: "))
    years = int(input("Ingrese el numero de años: "))

    for i in range(years):
        capital = cantidad * (1 + (interes / 100)) ** (i + 1)
        print(f"Su capital en el año {i + 1} es : {capital}")


"""
EJERCICIO 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""


def ejercicio6():
    numero = int(input("Ingrese el numero: "))
    caracter = "*"
    while numero > 0:
        print(caracter)
        caracter += "*"
        numero -= 1


"""
EJERCICIO 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""


def ejercicio7():
    print("Tablas de multiplicar del uno al 10")
    for i in range(1, 10):
        for j in range(10):
            print(f"{i} x {j} = {i * j} "
                  f"")
        print("\n")


"""
EJERCICIO 8 ****
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""


def ejercicio8():
    numero = int(input("Ingrese un numero: "))
    for i in range(1, numero + 1, 2):
        for j in range(i, 0, -2):
            print(j, end="")
        print("")


"""
EJERCICIO 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""


def ejercicio9():
    key = "MerequEtengue02424"
    bandera = False
    while not bandera:
        key_prueba = input("Ingrese su contraseña: ")
        if key_prueba == key:
            print("Contraseña correcta")
            bandera = True
        else:
            print("Contraseña incorrecta")
            pass


"""
EJERCICIO 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""


def ejercicio10():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 != 0:
        print(f"{numero} es primo")


"""
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
las letras de la palabra introducida empezando por la última.
"""


def ejercicio11():
    palabra = input("Ingrese una cadena de texto: ")
    for caracter in palabra[::-1]:
        print(caracter)


"""
EJERCICIO 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
pantalla el número de veces que aparece la letra en la frase.
"""


def ejercicio12():
    contador = 0
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    for caracter in frase:
        if caracter == letra:
            contador += 1
    print(f"La frase: '{frase}', tiene la letra: '{letra}' {contador} veces")


"""
EJERCICIO 12 + 1
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará.
"""


def ejercicio13():
    bandera = False
    while not bandera:
        clave = "salir"
        frase = input("Habla: ")
        if frase != clave:
            print(frase)
        else:
            bandera = True
