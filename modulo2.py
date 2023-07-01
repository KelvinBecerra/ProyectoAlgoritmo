#Importaciones
from principal import*
from menu import *
from modulo1 import *
from modulo3 import *
from modulo4 import *
from modulo5 import *
from modulo6 import *



def registrar_clientes():
    productos = []
    nombre = input("Ingrese su nombre: ")
    cedula = ''
    while cedula[0] != "V" or cedula[0] != "J":
        cedula = input("Ingrese su cedula (Inicie con una V para natural o J para juridico, sin espacios)': ")
    nombre_producto = ''
    while nombre_producto != '0':
        nombre_producto = input("Ingrese el nombre del producto a agregar, para terminar de agregar escriba '0' aqui: ")
        cantidad = input("Ingrese la cantidad de productos a agregar: ")
        if buscar_producto(nombre_producto, cantidad):
            producto = {}
            producto['nombre'] = nombre_producto
            producto['cantidad'] = cantidad
            productos.append(producto)
    for product in productos:
        compra_producto(product['nombre'], product['cantidad'])
        
#Funcion de guardado de base de datos
def check_clientes():
    
    #Convirtiendo un db de json a objetos
    def db_a_objetos(base_de_datos):
        db = []
        for cliente in base_de_datos:
            db.append(Comprador(producto["nombre"],producto["descripcion"],producto["precio"],producto["categoria"],producto["stock"],producto["ventas"]))
        return db

    #convirtiendo base de datos a json para guardarla en el txt
    def convertir_a_json(base_de_datos):
        db = []
        for producto in base_de_datos:
            objeto = {}
            objeto['nombre'] = producto.nombre
            objeto['descripcion'] = producto.descripcion
            objeto['precio'] = producto.precio
            objeto['categoria'] = producto.categoria
            objeto['stock'] = producto.stock
            objeto['ventas'] = producto.ventas
            db.append(objeto)
        return db

    filename = "clientes.txt"
    #Intenta leer el archivo "clientes.txt"
    try:
        with open(filename, 'r') as file:
            content = file.read()
            db = db_a_objetos(eval(content))
        print("Base de datos cargada correctamente")
    
    #Si se genera el error "FileNotFoundError" entonces se crea el archivo halando la info de github        
    except FileNotFoundError:
        
        db = convertir_a_json(url_a_objetos())
        with open(filename, 'w') as file:
            file.write(str(db))
        print("Primera vez")
        
    return db
    


lista_clientes={}
def registrar_ventas():
    registrar_clientes()
    productos_comprados=int(input("Ingresar la cantidad de productos comprados: "))
    


#def calculos():
def menu_ventas():
    pass

#total=(producto.precio*productos_comprados)
# El desglose del total de compra
# Subtotal 
# Descuentos
# 5% de descuento si el cliente es jurídico y paga de contado 
# IVA (16%)
# IGTF (3%) en caso de que pague en divisas
# Total
# Generar facturas para cada compra
# Si el cliente es jurídico se podrá realizar compras a crédito (pago en 15 o 30 días)
# Buscar ventas en función de los siguientes filtros:
# Cliente
# Fecha de la venta	
# Monto total de la venta