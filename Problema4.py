class rectangulo:
    def __init__(self, ancho , largo):
        self.ancho = ancho
        self.largo = largo 
    
    def calculaArea(self):
        area = self.ancho * self.largo
        print("El area del rectangulo es: ", area)

anch = float(input("Ingresa el ancho del rectangulo: "))
larg = float(input("Ingresa el largo del rectangulo: "))
square = rectangulo(anch,larg)
square.calculaArea()

    