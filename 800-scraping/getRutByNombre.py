# Importar módulos
from numpy import number
import requests
import csv
from bs4 import BeautifulSoup



def getRutByNombre(nombre):

    nombre_mas = nombre.replace(" ", "+")
    print(nombre)
    # Definir la URL
    # url = "https://www.google.com/search?q=portalchile.cl+FLUIDOS+Y+MECANICA+FLUMEC+LIMITADA"

    url = "https://www.google.com/search?q=portalchile.cl+" + nombre_mas
    
    # Ejecutar GET-Request
    response = requests.get(url)

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    # print('html.................................................')
    # print(html)

    # Convierte el texto HTML en un string
    html_text = html.text

    vector = html_text.split(nombre)
    rut = 0
    for cadena in vector:
        # print(i)
        l = cadena.find('RUT')
        if l != -1:
            for i in range(3,10):
                
                if cadena[l+i].isnumeric():
                    # print(cadena[l+i:l+i+10])
                    rut = cadena[l+i:l+i+10]
                    break
        if rut != 0:
            break
            
    # print('rut.................................................')
    # print(rut)

    return rut



