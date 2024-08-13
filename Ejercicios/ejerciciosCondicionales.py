"""
EJERCICIO 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""


def ejercicio1():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("No eres menor de edad")


"""
EJERCICIO 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la 
variable sin tener en cuenta mayúsculas y minúsculas.
"""


def ejercicio2():
    key = "HolaMundo"
    contrasena = input("Ingrese la contraseña")
    if key.lower() == contrasena.lower():
        print("La contraseña es correcta")


"""
EJERCICIO 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""


def ejercicio3():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    if divisor != 0:
        print(f"El resultado de {divisor} / {dividendo} = {divisor / dividendo}")
    else:
        print("ERROR EL DIVISOR ES 0")


"""
EJERCICIO 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""


def ejercicio4():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print(f"El numero {numero} es par ")
    else:
        print(f"El numero {numero} es impar")


"""
EJERCICIO 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € 
mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el 
usuario tiene que tributar o no.
"""


def ejercicio5():
    edad = int(input("Ingrese su edad: "))
    ingresos = int(input("Ingrese sus ingresos mensuales: "))
    if edad > 16 and ingresos > 1000:
        print("Lo siento debes declarar al fisco")
    else:
        print("Todo en orden no debes pagar impuestos")


"""
EJERCICIO 6 
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
grupo que le corresponde.
"""


def ejercicio6():
    grupo_a = "abcdefghijklm"
    grupo_b = "nñopqrstuvwxyz"
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo M o H: ")
    if (nombre[0].lower() in grupo_a and sexo.lower() == "m") or (nombre[0].lower() in grupo_b and sexo.lower() == "h"):
        print(f"{nombre} usted pertenece al grupo A")
    else:
        print(f"{nombre} usted pertenece al grupo B")


"""
EJERCICIO 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde
"""


def ejercicio7():
    renta = int(input("Ingrese su renta anual: "))
    if renta > 60000:
        print("Le corresponde un impositivo del 45% ")
    elif 35000 < renta <= 60000:
        print("Le corresponde un impositivo del 30%")
    elif 20000 < renta <= 35000:
        print("Le corresponde un impositivo del 20%")
    elif 10000 < renta <= 20000:
        print("Le corresponde un impositivo del 15%")
    else:
        print("Le corresponde un impositivo del 5%")


"""
EJERCICIO 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener 
en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre 
las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero 
conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de 
dinero que recibirá el usuario.
"""


def ejercicio8():
    puntucacion = float(input("Ingrese su puntiacion: "))
    if puntucacion >= 0.6:
        print(f"Su nivel de rendimiento es Meritorio, usted recibe {puntucacion * 2400}")
    elif 0.4 <= puntucacion < 0.6:
        print(f"Su nivel de rendimiento es Aceptable, usted recibe {puntucacion * 2400}")
    else:
        print(f"Su nivel de rendimiento es Inaceptable, usted recibe {puntucacion * 2400}")


"""
EJERCICIO 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del 
cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 
años debe pagar 5€ y si es mayor de 18 años, 10€.
"""


def ejercicio9():
    edad_cliente = int(input("Ingrese la edad del cliente: "))
    if edad_cliente >= 18:
        print(f"Usted paga: {10}$")
    elif 4 <= edad_cliente < 18:
        print(f"Usted paga: {5}$")
    else:
        print(f"Entrada ¡GRATIS!")


"""
EJERCICIO 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes 
para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la 
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva.
"""


def ejercicio10():
    print("¿Que tipo de pizza desea? \nVegetariana (1) \nNo vegetariana (2) :")
    tipo_pizza = int(input("Ingrese su opcion: "))
    if tipo_pizza == 1:
        print("Menu de ingredientes para pizza vegetariana \nPimiento (p) \nTofu (t)")
        ingredientes = input("Seleccione sus ingredientes: ")
        if ingredientes.lower() == "p":
            print(f"Su pizza lleva Pimiento, mozzarella y tomate")
        elif ingredientes.lower() == "t":
            print(f"Su pizza lleva tofu, mozzarella y tomate")
        else:
            print("Esa opcion no existe")
    else:
        print("Menu de ingredientes para pizza no vegetariana \nPeperoni (p) \nJamon (j) \nSalmon (s) ")
        ingredientes = input("Seleccione sus ingredientes: ")
        if ingredientes.lower() == "p":
            print(f"Su pizza lleva Peperoni, mozzarella y tomate")
        elif ingredientes.lower() == "j":
            print(f"Su pizza lleva Jamon, mozzarella y tomate")
        elif ingredientes.lower() == "s":
            print(f"Su pizza lleva Salmon, mozzarella y tomate")
        else:
            print("Esa opcion no existe")


ejercicio10()
