# Circulo area y perimetro
import math

def circulo_area_perimetro():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    print("Área:", area)
    print("Perímetro:", perimetro)

circulo_area_perimetro()