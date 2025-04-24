# Precio con iva 

def precio_con_iva():
    precio = float(input("Ingrese el precio del producto: "))
    precio_final = precio * 1.19
    print("Precio final con IVA (19%):", precio_final)

precio_con_iva()