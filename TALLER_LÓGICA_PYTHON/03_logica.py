
def count_list_for():
    
    numeros = [1,2,3,4,5,6,7,8,9,10]

    print("Bucle: For")
    print("--"*50)
    for x in numeros:
        print(x)
    print("--"*50)

count_list_for()
    


def count_list_while():

    numeros = [1,2,3,4,5,6,7,8,9,10]
    indice = 0 

    print("Bucle: While")
    print("--"*50)
    while indice < len(numeros):
        print(numeros[indice])
        indice += 1
    print("--"*50)

count_list_while()