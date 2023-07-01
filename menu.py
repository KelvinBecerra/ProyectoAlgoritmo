from principal import*
from modulo1 import*
from modulo2 import*
from modulo3 import*
from modulo4 import*
from modulo5 import*
from modulo6 import*
class Producto():#MODULO 1
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
class Comprador:#MODULO 2
    def __init__(self,nombre,cedula,productos,metodo_pago,metodo_envio):
        self.nombre=nombre
        self.cedula=cedula
        self.productos=productos
        self.metodo_pago=metodo_pago
        self.metodo_envio=metodo_envio
    def __str__(self):
        return f"Nombre: {self.nombre}\n Cedula: {self.cedula}\n Productos: {self.productos}\n Metodo de pago: {self.metodo_pago}\n Metodo de envio: {self.metodo_envio}"

class Clientes:#MODULO 3
    def __init__(self,nombre,apellido,razon_social,tipo_cliente,cedula,rif,correo,direccion_envio,telefono):
       self.nombre=nombre
       self.apellido=apellido
       self.razon_social=razon_social
       self.tipo_cliente=tipo_cliente
       self.cedula=cedula
       self.rif=rif
       self.correo=correo
       self.direccion_envio=direccion_envio
       self.telefono=telefono
    def __str__(self):
        return f"Nombre: {self.nombre}\n Apellido: {self.apellido} \n Razon social: {self.razon_social} \n Tipo de cliente: {self.tipo_cliente} \n Cedula: {self.cedula} \n RIF: {self.rif}\n Correo: {self.correo} \n Direccion de envio: {self.direccion_envio}\n Telefono: {self.telefono}"

class Pagos():#MODULO 4
    def __init__(self,monto,moneda,tipo_pago,buscar_pagos,fecha,):
        self.monto=monto
        self.moneda=moneda
        self.tipo_pago=tipo_pago
        self.buscar_pagos=buscar_pagos
        self.fecha=fecha
    def __str__(self):
        return f"Monto: {self.monto}\n Moneda: {self.moneda}\n Tipo de pago: {self.tipo_pago}\n Buscar pago: {self.buscar_pagos}\n Fecha: {self.fecha}"
    
def main_principal():
    print("---- BIENVENIDO A LA TIENDA DE PRODUCTOS NATURALES----")
    print("¿Que deseas hacer?")
    print(f" (1) Gestión de producto\n (2) Gestion de ventas\n (3) Gestion de clientes\n (4) Gestion de pagos\n (5) Gestion de envios\n (6) Indicadores de gestion")
    opcion=int(input("--> "))
    if opcion==1:
        menu_productos()
    elif opcion==2:
        pass
        #menu_ventas() falta
    elif opcion==3:
        menu_clientes()
    elif opcion==4:
        menu_pagos()
    elif opcion==5:
        menu_envio()
    elif opcion==6:
        menu_estadisticas()    
