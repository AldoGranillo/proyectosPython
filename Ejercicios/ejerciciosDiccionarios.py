"""
EJERCICIO 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def ejercicio1():
    monedas = {
        'Euros': '€',
        'Dollar': '$',
        'Yen': '¥'
    }
    divisa = input("Ingrese el nombre de la divisa que desea: ")
    print(monedas.get(divisa, "la divisa no esta en el diccionario"))


"""
EJERCICIO 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> 
y su número de teléfono es <teléfono>.
"""


def ejercicio2():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    direccion = input("Ingrese su direccion: ")
    telefono = int(input("Ingrese su numero telefonico: "))
    almacen = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
    print(f"{almacen.get('nombre')} tiene {almacen.get('edad')}, vive en {almacen.get('direccion')} y su numero "
          f"de telefono es {almacen.get('telefono')}")


"""
EJERCICIO 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por 
una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""


def ejercicio3():
    precios_fruta = {
        'Platano': 1.35,
        'Manzana': 0.80,
        'Pera': 0.85,
        'Naranja': 0.70
    }
    fruta = input("Ingrese una fruta: ")
    kilos = int(input("Ingrese cuantos kilos quieres: "))
    print(precios_fruta.get(fruta.title(), "La fruta no se encuentra") * kilos)


"""
EJERCICIO 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato 
dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""


def ejercicio4():
    meses = {
        '01': 'enero',
        '02': 'febrero',
        '03': 'marzo',
        '04': 'abril',
        '05': 'mayo',
        '06': 'junio',
        '07': 'julio',
        '08': 'agosto',
        '09': 'septiempre',
        '10': 'octubre',
        '11': 'noviembre',
        '12': 'diciembre'
    }
    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
    dia, mes, ano = fecha.split("/")
    print(f"{dia} de {meses.get(mes)} del {ano}")


"""
EJERCICIO 5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en 
el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""


def ejercicio5():
    creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    for key, values in creditos.items():
        print(f"{key} tiene {values} creditos")


"""
EJERCICIO 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""


def ejercicio6():
    diccionario = {}
    for i in range(10):
        nombre = input("Ingrese su nombre: ")
        diccionario[i] = nombre
        print(diccionario)


"""
EJERCICIO 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""


def ejercicio7():
    bandera = False
    cesta = {}
    while not bandera:
        condicional = input("¿Quieres agregar un producto? (S/N)")
        if condicional.upper() == 'S':
            producto = input("Ingrese su producto: ")
            precio = float(input("Ingrese el precio: "))
            cesta[producto] = precio
        else:
            bandera = True
    print("Lista compras: ")
    contador = 0
    for key, value in cesta.items():
        print(f"{key} {value}")
        contador += value
    print(f"Coste total {contador}")


"""
EJERCICIO 8 ***
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en 
español e inglés separadas por dos puntos, y cada par de palabras seran separados por comas. 
El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y 
utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


def ejercicio8():
    traduccion = {}
    frases = input("Igrese sus palabras con la siguiente estructura: español:ingles,español:ingles : ")
    frase_pares = frases.split(",")
    for i in range(len(frase_pares)):
        clave, valor = frase_pares[i].split(":")
        traduccion[clave] = valor
    frase_traduccion = input("Ingrese la frase a traducir: ")
    for palabra in frase_traduccion.split():
        if palabra in traduccion:
            print(traduccion[palabra], end=" ")
        else:
            print(palabra, end=" ")
    print(traduccion)


"""
EJERCICIO 9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un 
diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada 
operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""


def ejercicio9():
    facturas = {}
    print(f"Bienvenido seleccione una opcion: \n1.-Añadir nueva factura \n2.-Pagar facuta \n3.-Terminar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        cont = 0
        numero_factura = int(input("Ingrese el numero de factura: "))
        coste_factura = int(input("Ingrese el coste de la factura: "))
        facturas[numero_factura] = coste_factura
        for key, values in facturas.items():
            cont += values
        print(f"Falta por pagar {cont}")
    elif opcion == 2:
        numero_fac = int(input("Ingrese el numero de la factura a pagar: "))
        print(f"Se cobro {facturas.get(numero_fac)}")
        facturas.pop(numero_fac)
    else:
        pass


"""
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será 
otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá 
el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente 
menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""


def ejercicio10():
    clientes = {}
    opcion = ""
    print("Bienvenido seleccione su opcion: \n(1) Añadir cliente \n(2) Eliminar cliente \n(3) Mostrar cliente "
          "\n(4) Listar todos los clientes \n(5) Listar clientes preferentes \n(6) Terminar")
    while opcion != 6:
        if opcion == 1:
            clave = input("Ingrese el NIF: ")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la direccion: ")
            telefono = input("Ingrese el teleforno: ")
            correo = input("Ingrese el correo: ")
            preferente = input("Es preferente S/N: ")
            if preferente.upper() == 'S':
                clientes[clave] = {'nombre': nombre, 'direccion': direccion, 'teleforno': telefono, 'correo': correo,
                                   'preferente': True}
            else:
                clientes[clave] = {'nombre': nombre, 'direccion': direccion, 'teleforno': telefono, 'correo': correo,
                                   'preferente': False}
        elif opcion == 2:
            nif = input("Ingrese el nif del cliente: ")
            clientes.pop(nif)
        elif opcion == 3:
            nif = input("Ingrese el nif del cliente: ")
            print(clientes.get(nif))
        elif opcion == 4:
            print(clientes)
        elif opcion == 5:
            nif = input("Ingrese el nif del cliente:xvdvs ")
            if clientes.get(nif):
                print(nif, clientes[nif].get('nombre'))
        else:
            pass
        opcion = int(input("Ingrese su opcion: "))


"""
EJERCICIO 11 ****
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada 
línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos 
con la información contenida en el directorio.
Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a 
un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. 
Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la 
información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5},
'71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0},
'63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, 
'98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
"""


def ejercicio11():
    directorio = {}
    cadena = ("nif;nombre;email;teléfono;descuento\n01234567L;Luis "
              "González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena "
              "Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José "
              "Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7")
    cad_v1 = cadena.split("\n")
    campos = cad_v1[0].split(";")
    print(campos)
    for i in cad_v1[1:]:
        cliente = {}
        lista_datos = i.split(";")
        for j in range(1, len(lista_datos)):
            cliente[campos[j]] = lista_datos[j]
        directorio[lista_datos[0]] = cliente
    print(directorio)

