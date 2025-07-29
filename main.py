#librerias

import random as r

# coding: utf-8

print("¡Bienvenido al juego de Adivinar el Número!\n")  
print("Estoy pensando en un número secreto entre 1 y 100.\n")  
print("Tu misión es adivinarlo. ¡Tienes 10 intentos!\n\n")

print("Después de cada suposición, te daré una pista para que sepas si el número secreto es mayor o menor.\n\n")

print("¡Mucha suerte! ¡Que empiece el juego!\n")

numero_secreto = r.randint(1, 100)

numero_del_usuario = int(input("Introduce un número entre 1 y 100: "))

intentos = 10

while intentos > 0:
    if numero_del_usuario < numero_secreto:
        print("El número secreto es mayor que", numero_del_usuario)
    elif numero_del_usuario > numero_secreto:
        print("El número secreto es menor que", numero_del_usuario)
    else:
        print("¡Felicidades! Has adivinado el número secreto:", numero_secreto)
        break
    intentos -= 1
    if intentos > 0:
        numero_del_usuario = int(input(f"Te quedan {intentos} intentos. Introduce otro número entre 1 y 100: "))
    else:
        print("Lo siento, has agotado tus intentos. El número secreto era:", numero_secreto)
        break
