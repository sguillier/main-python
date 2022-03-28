# Importar módulos
from numpy import number
import requests
import csv
from bs4 import BeautifulSoup


def getNombreByRut(rut):

    # Definimos url_rut
    con_rut = '"con+RUT+' + str(rut) + '"'

    # Definir la URL
    url = "https://www.google.com/search?q=portalchile.cl+" + con_rut
 
    # Ejecutar GET-Request
    response = requests.get(url)

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    # print('html.................................................')
    # print(html)

    # Convierte el texto HTML en un string
    html_text = html.text
    print('html_text.................................................')
    print(html_text)

    vector = html_text.split('con RUT '+ str(rut))
    # print(len(vector))
    # print('////////////////////////////////////////////////////////////')

    nombre = ''
    print('largo', len(vector))
    
    if len(vector) > 2:
        for cadena in vector:
            largo = len(cadena)
            
            print('cadena.................................................')
            print(cadena)
            for i in range(1, min(200,largo)):
                j = largo - i
                # print(largo, ' ', i, ' ', j , ' ' , cadena[j:j+29])
                if cadena[j:j+29] == 'resultadosPalabra por palabra':
                    nombre = cadena[j+29:largo]
                    break

            if nombre != '':
                break

    # # print('rut.................................................')
    # # print(rut)

    return nombre


# print(getNombreByRut('96592740-9'))
