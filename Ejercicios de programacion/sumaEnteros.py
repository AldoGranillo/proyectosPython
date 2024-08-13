"""
Escribir un programa que lea un entero positivo,n
introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
"""


def sumaEnteros():
    # solicitar el numero
    numero = int(input("Ingrese el numero: "))
    # calcular la suma
    suma = (numero * (numero + 1)) // 2  # Para que sea division entera //
    # imprimir el resultado
    print(f"La suma de los enteros positivos de {numero} es {suma}")


"""
Palabra palindroma 
Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma 
leída de izquierda a derecha que de derecha a izquierda; por ejemplo, anilina; dábale arroz a la zorra el abad.
"""

palabra = input("Ingrese su palabra :) ")
palabraInv = ""
for i in (palabra[::-1]):
    palabraInv += i
if palabra == palabraInv:
    print(f"{palabra} es palindroma {palabraInv}")
else:
    print("No es palindroma")
