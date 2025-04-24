

def registro_clientes():
    
    db_clientes = []
    
    while True:

        opcion = int(input("Registrar cliente: 1 \n Consultar cliente: 2 \n  Salir: 3 \n Ingrese una opcion: "))
        
        if opcion == 1:
            
            print("Para Registrar cliente ingrese: Documento, Nombre, Apellido, Edad ")
            
            id = input("Ingrese Documento: ")
            name = input("Ingrese Nombre: ")
            last_name = input("Ingrese Apellido: ")
            age = input("Ingrese Edad: ")
            height = input("Ingrese la Estatura: ")
            weight = input("Ingrese el peso: ")
            
            cliente = {
                "Documento": id,
                "Nombre": name,
                "Apellido": last_name,
                "Edad": age,
                "Altura": height,
                "Peso": weight
                }
            
            db_clientes.append(cliente)
            
            print("- - - - Registro Exitoso - - - - ")
            

        if opcion == 2:
            
            consult = input("ingrese el documento: ")
    
            for cliente in db_clientes:
                cliente.get("Documento")
                if consult == cliente.get("Documento"):
                    print(cliente)
            else:
                print("El cliente no registra ")

        if opcion == 3:
            print("--- saliendo del programa ---")
            break

registro_clientes()