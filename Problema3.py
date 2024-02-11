import math 
class circulo:
    def __init__(self, radio):
        self.radio = radio 

    def CalcArea(self):
        a = math.pi * self.radio**2 
        print("El area es: ", a)

r=float(input("Ingrese el radio: "))
circ1 = circulo(r)
circ1.CalcArea()
    

        
