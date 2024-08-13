"""
EJERCICIO 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla
en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""


def ejecicio1():
    nombre_user = input("Ingrese su nombre: ")
    numero = int(input("Ingrese un numero: "))

    for i in range(numero):
        print(nombre_user)


"""
EJERCICIO 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y 
después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y 
otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""


def ejercicio2():
    nombre = input("Ingrese su nombre: ")
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.title())


"""
EJERCICIO 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número 
de letras que tienen el nombre.
"""


def ejercicio3():
    nombre = input("Ingrese su nombre: ")
    print(f"{nombre.upper()} tiene {len(nombre)} ")


"""
EJERCICIO 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país
+34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un 
número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""


def ejercicio4():
    print("Recuerde que el formato es : +34-913724710-56")
    numero = input("Ingrese el numero: ")
    numero_sn_extension = numero.split("-")
    print(numero_sn_extension[1])


"""EJERCICIO 5 Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
la frase invertida."""


def ejercicio5(text):
    cadenainv = ""
    if text:
        for i in (text[::-1]):
            cadenainv += i
        return cadenainv
    else:
        return ""


"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por 
pantalla la misma frase pero con la vocal introducida en mayúscula.
"""


def ejercicio6():
    frase = input("Ingrese una frase: ")
    vocal = input("Ingrese una vocal en minusculas: ")
    if vocal in frase:
        print(frase.replace(vocal, vocal.upper()))


"""
EJERCICIO 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro 
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""


def ejercicio7():
    correo = input("Ingrese su correo electronico: ")
    x = correo.split("@")
    print(x[0] + "ceu.es")


"""
EJERCICIO 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre 
por pantalla el número de euros y el número de céntimos del precio introducido.
"""


def ejercicio8():
    precio = input("Ingrese el precio con decimales: ")
    x = precio.split(".")
    print(f"Su producto vale {x[0]} euros con {x[1]} centavos")


"""
EJERCICIO 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan 
con un solo carácter.
"""


def ejercicio9():
    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
    print(f"Dia {fecha[0:2]} \nMes {fecha[2:4]} \nAño {fecha[4:]}")


"""
EJERCICIO 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta.
"""


def ejercicio10():
    lista_compras = input("Ingrese su lista de productos separados por comas: ")
    lista_separada = lista_compras.split(",")
    for prudcto in lista_separada:
        print(f"Usted compro : {prudcto}")


"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla 
una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""


def ejercicio11():
    producto = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio: "))
    unidades = int(input("Ingrese el numero de unidades de productos comprados: "))
    print(f"{producto}: {unidades} unidades x {precio}$ = {unidades * precio}$")


ejercicio11()
