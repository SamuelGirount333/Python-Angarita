def elementos_repetidos(arr1, arr2):
    repetidos = []
    for elem in arr1:
        if elem in arr2:
            repetidos.append(elem + elem)
    return repetidos

print(elementos_repetidos(["s", "w", "@", "3", "a", "p"], ["#", "p", "a", "z", "@"]))