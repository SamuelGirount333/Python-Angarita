array =  [1,2,3,4,5,6,7,8,9,10]

while True:    
    def agregar_elementos(list:list):
        print(list)
        question = int(input("Que elemento desea agregar Palabras= 1, Numeros= 2, boolean= 3, Exit= 4: "))
        if question == 1:
            new_item_str = input("ingrese la palabra que desea agregar: ")
            list.append(new_item_str)
            print(list)
        if question == 2:
            new_item_int = int(input("ingrese el numero que desea agregar: "))
            list.append(new_item_int)
            print(list)
        elif question == 3:
            new_item_bool = bool(input("ingrese el Booleano que desea agregar: "))
            list.append(new_item_bool)
            print(list)
        else:
            print("saliendo del programa...")
    
    agregar_elementos(array)