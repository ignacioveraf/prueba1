import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
consulta = json.loads(response.text)

def georeference(n):
    lista = []
    print("ingrese un numero:")
    n=(input())
    nombre= (consulta[int(n)]['name'])
    lat = (consulta[int(n)]['address']['geo']['lat'])
    lng = (consulta[int(n)]['address']['geo']['lng'])
    lista.append([nombre,lat,lng])
    print(lista)
n=0
georeference(n)

