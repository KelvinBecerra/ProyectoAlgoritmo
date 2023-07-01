#Exportaciones
from menu import Producto
from principal import cargar_productos

def guardar_db(base_de_datos):
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
    
    filename = "db.txt"    
    db = convertir_a_json(base_de_datos)
    with open(filename, 'w') as file:
        file.write(str(db))
    print("Cambios guardados exitosamente!")

#Funcion de guardado de base de datos
def check_db():
    
    #convirtiendo base de datos de github a objetos
    def url_a_objetos():
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json"
        db=[]
        response=cargar_productos(url)
        for producto in response:
            db.append(Producto(producto["name"],producto["description"],producto["price"],producto["category"],10,0))
        return db
    
    #Convirtiendo un db de json a objetos
    def db_a_objetos(base_de_datos):
        db = []
        for producto in base_de_datos:
            db.append(Producto(producto["nombre"],producto["descripcion"],producto["precio"],producto["categoria"],producto["stock"],producto["ventas"]))
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

    filename = "db.txt"
    #Intenta leer el archivo "db.txt"
    try:
        with open(filename, 'r') as file:
            content = file.read()
            db = db_a_objetos(eval(content))
        #print("Base de datos cargada correctamente")
    
    #Si se genera el error "FileNotFoundError" entonces se crea el archivo halando la info de github        
    except FileNotFoundError:
        
        db = convertir_a_json(url_a_objetos())
        with open(filename, 'w') as file:
            file.write(str(db))
        #print("Primera vez 😉")
        
    return db
    
#Funcion para agregar un producto
def agregar_producto():
    nombre=input("Ingrese el nombre del producto: ").title()
    descripcion=input("Ingrese la descripción del producto: ")
    precio=float(input("Precio del producto: "))
    categoria=input("¿A que categoria pertenece el producto?: ")
    inventario=int(input("¿Cuantos productos son?: "))
    ventas=int(input("¿Cuantas veces vendidas?: "))
    db.append(Producto(nombre,descripcion, precio,categoria,inventario,ventas))
    print (f"{nombre} Se ha añadido correctamente")

    
#Funcion para buscar un producto

def buscar_producto():
    
    print("----BUSCADOR DE PRODUCTOS----")
    print(" (1) Buscar por nombre\n (2) Buscar por categoria\n (3) Buscar por precio \n (4) Disponibilidad ")
    opcion=int(input("--> "))
    if opcion==1:#Busco por nombre
        #variable para validar que esté o no esté
        validar_nombre=False
        buscar_nombre=input("Ingresar nombre del producto: ").title()
        
        for producto in db:
            if producto.nombre==buscar_nombre.title():
                validar_nombre=True
                print(producto)
                
        if validar_nombre==True:
            print("PRODUCTO ENCONTRADO")
        else:
            print("¡PRODUCTO NO ENCONTRADO!")
                
    elif opcion==2:#Busco por categoria
        buscar_categoria=input("¿A que categoria pertenece el producto?")
        for producto in db:
            if producto.categoria==buscar_categoria.title():
                validar_nombre=True
                
                print(producto)
        if validar_nombre==True:
            print("PRODUCTO ENCONTRADO")
        else:
            print("¡PRODUCTO NO ENCONTRADO!")
            
    elif opcion==3:#Busco por precio
        buscar_precio=int(input("Ingrese un rango de precios: "))
        for producto in db:
            if producto.precio==buscar_precio:
                validar_nombre=True
                print(producto)
        if validar_nombre:
            print("PRODUCTO ENCONTRADO")
        else:
            print("¡PRODUCTO NO ENCONTRADO!")
            
    elif opcion==4:#Ver disponibilidad del inventario
        buscar_nombre=input("Ingrese el nombre del producto: ").title()
        for producto in db:
            print(producto.stock)
            break
 

def modificar_informacion():
    nombre=input("Ingresa el nombre del producto: ").title()
    for producto in  db:
        if nombre==producto.nombre:
            print(f"¿Que deseas modificar de {producto}?: ")
            print(f" (1) Nombre\n (2) Categoria\n (3) Descripción\n (4) Precio\n (5) Inventario \n (6) Ventas")
            opcion=int(input("--> "))
            if opcion==1:
                producto.nombre=input("Ingresa el nuevo nombre: ").title() #Aqui cambio el nombre
                print(producto)
            elif opcion==2:
                producto.categoria=input("Ingresa la nueva categoria: ").title() #Aqui cambio la categoria
                print(producto)
            elif opcion==3:
                producto.descripcion=input("Ingresa la nueva descripcion: ").title()#Aqui cambio la descripcion
                print(producto)
            elif opcion==4:
                producto.precio=int(input("Ingresa el nuevo precio: "))#Aqui cambio la categoria
                print(producto)
            elif opcion==5:
                producto.inventario=int(input("Ingresa la nueva cantidad: "))#Aqui cambio la categoria
                print(producto)
            elif opcion==6:
                producto.ventas=int(input("Ingrese la nueva cantidad de ventas: "))#Aqui cambio la categoria
                print(producto)
                
def eliminar_producto():
    
    existe = False
    buscar_producto=input("Ingrese el nombre del producto: ").title()            
    for producto in db:
        if producto.nombre == buscar_producto:
            existe = True
            db.pop()
            print("Producto eliminado")
    if not existe:
        print("No existe el producto")
    
        
        
        
#funcion para escoger que quiero hacer            
def menu_productos():
    while True:
        print(" (1) Agregar Productos\n (2) Buscar Productos\n (3) Modificar la informacion de algun producto\n (4) Eliminar producto\n (5) Salir")
        opcion=int(input("--> "))
        if opcion==1:
            agregar_producto()
        elif opcion==2:
            buscar_producto()
        elif opcion==3:
            modificar_informacion()
        elif opcion==4:
            eliminar_producto()
        elif opcion==5:
            guardar_db(db)
            break
global db
db = check_db()
menu_productos()

