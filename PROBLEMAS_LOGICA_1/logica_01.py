# Programa que determina la edad del usuario 

    
def propuesta_edad(**kwargs):
    sum_age = 15 
        
    name = input('ingrese su nombre: ')
    age = int(input('Ingres su edad actual: '))
    print('En 15 años usted tendra la siguiente edad: ')

    future_age = age + sum_age

    print(f"Usted {name} va tener en 15 años la siguente edad {future_age}")

propuesta_edad()


