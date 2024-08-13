"""
Juego en el que el usuario intenta adivinar un número generado aleatoriamente por el programa.
"""
#importar random
import random

print("Bienvenido pruebe adivinar el numero a la computadora :D")
#generar numero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

#pedir al usuario su numero
numero_usuario = int(input("Ingrese su numero: "))


#validar el numero
def validarValor(numero1, numero2):
    print("Pensando..........")
    if numero1 == numero2:
        print(f"Vaya usted es un genio, el numero de la computadora es {numero1} y usted dijo {numero2}")
    else:
        print(f"Mucha suerte en la proxima, el numero de la computadora es {numero1} y usted dijo {numero2}")


#imprimir el resultado
validarValor(numero_aleatorio, numero_usuario)
