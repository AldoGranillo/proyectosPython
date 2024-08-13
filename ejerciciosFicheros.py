from urllib import request
import os
"""
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla
de multiplicar de ese número, done n es el número introducido.
"""


def ejercicio1():
    numero = int(input("Ingrese un numero entero entre 1 y 10: "))
    fichero = open("tabla-n.txt", "w")
    for i in range(1, 11):
        fichero.write(str(numero) + "x" + str(i) + "=" + str(numero * i) + "\n")


#ejercicio1()
"""
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de 
ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje 
por pantalla informando de ello.
"""


def ejercicio2():
    ejercicio1()
    archivo = open("tabla-n.txt", "r")
    if archivo:
        print(archivo.read())
    else:
        print("El archivo al que desas acceder no existe")


"""
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de 
ese número, y muestre por pantalla la línea m del fichero. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""


def ejercicio3():
    ejercicio1()
    numeroLinea = int(input("Ingresa un numero entre 1 y 10: "))
    archivo = open("tabla-n.txt", "r")
    if archivo:
        xd = archivo.readlines()
        print(xd[numeroLinea])
    else:
        print("El archivo no existe")


"""
Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante su url y 
muestre por pantalla el número de palabras que contiene.
"""


def ejercicio4():
    try:
        fichero = request.urlopen('https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt')
        contenido = fichero.read()
        contenido = contenido.decode("utf-8")
        print(len(contenido))
    except Exception as err:
        print("Error", err)


"""
Ejercicio 6
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa incorporar funciones:
crear el fichero con el listín si no existe,
consultar el teléfono de un cliente, 
añadir el teléfono de un nuevo cliente,
eliminar el teléfono de un cliente. 
El listín debe estar guardado en el fichero de texto listin.txt donde
el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
"""


def crearListaTelefonos():
    fichero = open('listin.txt', 'w')
    registro = int(input("Ingrese cuantos registros desea añadir: "))
    for i in range(registro):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el numero telefonico: ")
        fichero.write(nombre + "," + telefono + "\n")
    return fichero


def añadirFichero():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    fichero = open('listin.txt','a')
    fichero.write(nombre + "," + telefono + "\n")

def consultarTelefono(nombre):
    fichero = open('listin.txt', 'r')
    elementos =[]
    for i in fichero:
        i.replace("\n", " ")
        elementos.append(i.split(","))
    print(elementos[0])

def ejercicio6():
    if os.path.exists('listin.txt'):
        print(
            "Bienvenido seleccione que es lo que desea hacer, \n(1)Añadir un nuevo telefono \n(2)Consultar un telefono "
            "\n(3)Eliminar un telefono \n(4)Salir")
        opcion = int(input(": "))
        if opcion == 1:
            añadirFichero()
        elif opcion == 2:
            nombre = input("Ingrese el nombre del cliente al que quiere consultar: ")
            consultarTelefono(nombre)

    else:
        print("Creando fichero")
        crearListaTelefonos()


ejercicio6()

