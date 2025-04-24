# Ejercicio 3


a = 2
b = 3.7


parte1 = 15 >= 7 * b


izquierda = 43 - 8 * 2 / 4
derecha = b * 5 / 2
parte2 = izquierda != derecha


resultado = parte1 or parte2


print("Parte 1 (15 >= 7 * b):", parte1)
print("Parte 2 ((43 - 8 * 2 / 4) != (b * 5 / 2)):", parte2)
print("Resultado final:", resultado)
