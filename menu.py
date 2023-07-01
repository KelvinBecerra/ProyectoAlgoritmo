class Producto():
    def __init__(self,nombre,descripcion,precio,categoria,stock,ventas):
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.categoria=categoria
        self.stock=stock
        self.ventas=ventas
    def __str__(self):
        return f"Nombre: {self.nombre}\n Descripcion: {self.descripcion}\n Precio: {self.precio}\n Categoria: {self.categoria}\n Stock: {self.stock}\n Ventas: {self.ventas}"
    def compra(self,cantidad):
        self.stock-=cantidad
        self.ventas+=cantidad
