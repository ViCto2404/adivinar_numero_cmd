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
