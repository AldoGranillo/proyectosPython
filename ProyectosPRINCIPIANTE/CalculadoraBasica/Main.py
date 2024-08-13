"""
@author : alsognilo

En este proyecto crearemos una calculadora en terminal :)
1 solicitar valores al usuario
"""

print("Ingrese sus valores por favor: ")
valor_uno = int(input("Ingrese el valor uno: "))
valor_dos = int(input("Ingrese el valor dos: "))
"""
2.- preguntar que operacion se quiere usar
Como en python no existe la estructura switch tocara usar if else
"""
print("Menu de operaciones \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division")
opcion = int(input("Ingrese el valor de la opcion: "))
if opcion == 1 :
    suma = (valor_uno +valor_dos)
    print(suma)
elif opcion == 2:
    resta = (valor_uno - valor_dos)
    print(resta)
elif opcion == 3:
    multiplicacion = (valor_uno * valor_dos)
    print(multiplicacion)
else :
    division = (valor_uno // valor_dos)
    print(division)
