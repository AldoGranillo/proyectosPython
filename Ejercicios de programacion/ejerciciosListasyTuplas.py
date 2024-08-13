"""
EJERCICIO 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia
y Lengua) en una lista y la muestre por pantalla.
"""


def ejercicio1():
    materias = input("Ingrese sus materias: ")
    # print(materias.split(" "))
    return materias.split(",")


"""
EJERCICIO 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia 
y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una 
de las asignaturas de la lista.
"""


def ejercicio2():
    lista_materias = ejercicio1()
    for i in lista_materias:
        print(f"Yo estudio {i} ")


"""
EJERCICIO 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y 
<nota> cada una de las correspondientes notas introducidas por el usuario.
"""


def ejercicio3():
    lista_materias = ejercicio1()
    lista_calificaciones = []
    for i in lista_materias:
        print(f"Ingresa calificacion para:  {i} ")
        calificacion = int(input(": "))
        lista_calificaciones.append(calificacion)
    for i in range(len(lista_materias)):
        print(f"En {lista_materias[i]} has sacado {lista_calificaciones[i]}")
    return lista_materias, lista_calificaciones


"""
EJERCICIO 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def ejercicio4():
    numeros_loteria = []
    num = int(input("Ingrese cuantos numeros ganadores hay: "))
    for i in range(num):
        numeros = int(input("Ingrese los numeros ganadores: "))
        numeros_loteria.append(numeros)
    numeros_loteria.sort()
    print(numeros_loteria)


"""
EJERCICIO 5
Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.
"""


def ejercicio5():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in (lista[::-1]):
        print(i, ",", end="")


"""
EJERCICIO 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia 
y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def ejercicio6():
    num_materias = int(input("Ingrese el numero de materias: "))
    materias = []
    calificaciones = []
    for i in range(num_materias):
        v1 = input("Ingrese su materia: ")
        v2 = int(input("Ingrese la calificacion de su materia: "))
        materias.append(v1)
        calificaciones.append(v2)

    for calificacion in calificaciones:
        if calificacion > 6:
            indice = calificaciones.index(calificacion)
            calificaciones.remove(calificacion)
            materias.pop(indice)

    for v1, v2 in zip(materias, calificaciones):
        print(f"Debes repetir {v1} porque sacaste {v2}")


"""
EJERCICIO 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""


def ejercicio7():
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]
    multiplos_de_tres = []
    print(f"Alfabeto original \n{abc}")
    for i in range(26):
        multiplos_de_tres.append((3 * (i + 1)))
    for letra, num in zip(abc, multiplos_de_tres):
        i = abc.index(letra)
        if i in multiplos_de_tres:
            abc.pop(i)
    print(abc)


"""
EJERCICIO 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""


def ejercicio8():
    palabra = input("Ingrese una frase: ")
    palabra_inv = ""
    for i in palabra[::-1]:
        palabra_inv += i
    if palabra == palabra_inv:
        print(f"{palabra} es un palindromo {palabra_inv}")
    else:
        print(f"{palabra} no es un palindromo {palabra_inv}")


"""
EJERCICIO 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""


def ejercicio9():
    vocales = ["a", "e", "i", "o", "u"]
    palabra = input("Ingrese una palabra: ")
    for i in vocales:
        contador = palabra.lower().count(i)
        print(f"La vocal {i} aparece {contador} veces")


"""
Ejercicio 10 
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y
muestre por pantalla el menor y el mayor de los precios.
"""


def ejercicio10():
    precios = [50, 75, 46, 22, 80, 65, 8]
    #Forma uno de resolver el ejercicio
    print(f"{precios}\nEl menor es {min(precios)} y el mayor es {max(precios)}")
    #Forma dos
    mini = maxi = precios[0]
    for precio in precios:
        if precio < mini:
            mini = precio
        elif precio > maxi:
            maxi = precio
    print(f"El minimo es {mini} y el maximo es {maxi} ")


"""
EJERCICIO 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y 
muestre por pantalla su producto escalar.
"""


def ejercicio11():
    vector1 = (1, 2, 3)
    vector2 = (-1, 0, 2)
    producto_escalar = 0
    for i in range(len(vector1)):
        producto_escalar += vector1[i] * vector2[i]
    print(f"El producto escalar de {vector1} y {vector2} es: {producto_escalar}")


"""
EJERCICIO 12
Escribir un programa que almacene las matrices
A=[ [1,2,3]
    [4,5,6]]
B=[ [-1, 0]
    [0, 1 ]
    [1, 1 ]]  
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
[[2 5]
[2 11]] 
"""


def ejercicio12():
    matriz_a = [[1, 2, 3], [4, 5, 6]]
    matriz_b = [[-1, 0], [0, 1], [1, 1]]
    matriz_ab = [[0, 0], [0, 0]]
    # El numero de columnas de A debe coincidir con el de filas de B
    if len(matriz_a) == len(matriz_b[0]):
        for i in range(len(matriz_a)):
            for j in range(len(matriz_b[i])):
                for k in range(len(matriz_b)):
                    matriz_ab[i][j] += matriz_a[i][k] * matriz_b[k][j]
    print(matriz_ab)


"""
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista 
y muestre por pantalla su media y desviación típica.
"""


def ejercicio13():
    muestra = input("Ingrese el tamaño de su muestra separados por comas: ")
    muestra_limpia = muestra.split(",")
    sumatoria = 0
    for numero in muestra_limpia:
        sumatoria += int(numero)
    media = sumatoria / len(muestra_limpia)
    print(media)

    sumatoria2 = 0
    for numero in muestra_limpia:
        sumatoria2 += (int(numero) - media) ** 2
    desviasion_tipica = (sumatoria2 / len(muestra_limpia)) ** 0.5

    print(desviasion_tipica)


ejercicio13()
