# Lanzamiento de dados
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    print("Suma:", dado1 + dado2)
