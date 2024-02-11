#%%
class Producto:
    def __init__(self, nombre, precio, año, marca):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} - {self.marca} ({self.año}) - ${self.precio}"

#%%
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el catálogo.")

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")


#%%
catalogo = Catalogo()

producto1 = Producto("Llantas", 200, 2023, "Michelin")
producto2 = Producto("Batería", 150, 2022, "Bosch")
producto3 = Producto("Frenos", 300, 2024, "Brembo")

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Mostrando todos los productos en el catálogo:")
catalogo.mostrar_productos()

print("\nFiltrando por año 2023:")
catalogo.filtrar_por_año(2023)


