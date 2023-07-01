from principal import*
from menu import*
from modulo1 import*
from modulo2 import*
from modulo4 import*
from modulo5 import* 
class Clientes:
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
clientes={}
def registrar_clientes():
    nombre=input("Ingrese nombre del cliente: ")
    apellido=input("Ingrese el apellido: ")
    razon_social=input("Ingrese razon social: ")
    tipo_cliente=input("Ingrese si es un cliente natural o juridico: ")
    cedula=int(input("Ingrese la cedula: "))
    rif=int(input("Ingrese el numero de rif: "))
    correo=input("Ingrese el correo electronico del cliente: ")
    direccion=input("Ingrese la direccion del envío: ")
    telefono=int(input("Ingrese el numero de telefono: "))
    clientes.append(Clientes(nombre,apellido,razon_social,tipo_cliente,cedula,rif,correo,direccion,telefono))
    print(f"Nuevo cliente añadido correctamente")
    
def modificar_informacion():
    correo=input("Ingresa el correo del cliente que quiere modificar: ")
    cedula=int(input("Ingrese la cedula del cliente que desea modificar: "))
    for cliente in clientes:
        if correo==cliente:
            print("¿Que desea modificar?")
            print(f" (1) Nombre\n (2)apellido\n (3)Razon social\n (4) Tipo de cliente \n (5) Cedula \n (6) RIF \n (7) Correo \n (8) Direccion de envio\n (9)Telefono ")
            opcion=input("--> ")
            if opcion==1:
                clientes.nombre=input("Ingrese el nuevo nombre: ")
                print(cliente)
            elif opcion==2:
                clientes.apellido=input("Ingrese el nuevo apellido: ")
                print(cliente)
            elif opcion==3:
                clientes.razon_social=input("Ingrese la nueva razon social: ")
                print(cliente)
            elif opcion==4:
                clientes.tipo_cliente=input("Ingrese el tipo de cliente: ")
                print(cliente)
            elif opcion==5:
                clientes.cedula=input("Ingrese la nueva cedula: ")
                print(cliente)
            elif opcion==6:
                clientes.rif=input("Ingrese el nuevo RIF: ")
                print(cliente)    
            elif opcion==7:
                clientes.correo=input("Ingrese el nuevo correo electronico: ")
                print(cliente)
            elif opcion==8:
                clientes.direccion=input("Ingrese la nueva direccion: ")
                print(cliente)
            elif opcion==9:
                clientes.telefono=input("Ingrese el nuevo numero de telefono: ")
                print(cliente) 
                
        elif cliente==cedula:
            print("¿Que desea modificar?")
            print(f" (1) Nombre\n (2)apellido\n (3)Razon social\n (4) Tipo de cliente \n (5) Cedula \n (6) RIF \n (7) Correo \n (8) Direccion de envio\n (9)Telefono ")
            opcion=input("--> ")
            if opcion==1:
                clientes.nombre=input("Ingrese el nuevo nombre: ")
                print(cliente)
            elif opcion==2:
                clientes.apellido=input("Ingrese el nuevo apellido: ")
                print(cliente)
            elif opcion==3:
                clientes.razon_social=input("Ingrese la nueva razon social: ")
                print(cliente)
            elif opcion==4:
                clientes.tipo_cliente=input("Ingrese el tipo de cliente: ")
                print(cliente)
            elif opcion==5:
                clientes.cedula=input("Ingrese la nueva cedula: ")
                print(cliente)
            elif opcion==6:
                clientes.rif=input("Ingrese el nuevo RIF: ")
                print(cliente)    
            elif opcion==7:
                clientes.correo=input("Ingrese el nuevo correo electronico: ")
                print(cliente)
            elif opcion==8:
                clientes.direccion=input("Ingrese la nueva direccion: ")
                print(cliente)
            elif opcion==9:
                clientes.telefono=input("Ingrese el nuevo numero de telefono: ")
                print(cliente)
        else:
            print("¡CLIENTE NO ENCONTRADO!")
            
                 
                    
                   
def eliminar_clientes():
    existe=False
    nombre=input("Ingrese el nombre del cliente que desea eliminar")
    for cliente in clientes:
        if cliente.nombre==nombre:
            existe=True
            clientes.pop()
            print("Cliente eliminado")
    if not existe:
        print("No existe el cliente")
            
def buscar_clientes():
    print("----BIENVENIDO AL BUSCADOR----")
    correo=input("Ingresa el correo del cliente que quiere modificar: ")
    cedula=int(input("Ingrese la cedula del cliente que desea modificar: "))
    for cliente in clientes: 
        if correo==cliente:
            print(cliente)
        elif cedula==cliente:
            print(cliente)
        else:
            print("¡CLIENTE NO ENCONTRADO!")
    
def menu_clientes():
    print("---BIENVENIDO AL MENU DE LOS CLIENTES----")
    print(f"(1) Registrar cliente\n (2) Modificar informacion de los clientes\n (3) Eliminar clientes \n (4) Buscar clientes ")
    opcion=int(input("--> "))
    if opcion==1:
        registrar_clientes()
    elif opcion==2:
        modificar_informacion()
    elif opcion==3:
        eliminar_clientes()
    elif opcion==4:
        buscar_clientes()
        
menu_clientes()