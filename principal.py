import json  #Importo la libreria Json
from urllib.request import urlopen #Se dice donde está y que voy a importar
def cargar_productos(url): #funcion para cargar el url
    response=urlopen(url)
    data_json=json.loads(response.read())
    return data_json