import requests
import json

response = requests.get('https://randomuser.me/api')

consulta = json.loads(response.text)

print(type(consulta))
print(consulta['results'][0]['name']['first'])
if consulta ['results'][0]['gender']== "male":
    print("el usuario es de sexo masculino:")
    print("Nombre:", consulta['results'][0]['name']['first'])
    print("Apellido:",consulta['results'][0]['name']['last'])
    print("Usuario:",consulta['results'][0]['login']['username'])
    print("Contraseña:",consulta['results'][0]['login']['password'])
    
else:
    print ("el usuario es de sexo femenino")
    print("Nombre:", consulta['results'][0]['name']['first'])
    print("Apellido:",consulta['results'][0]['name']['last'])
    print("Direccion + numero:",consulta['results'][0]['location']['street']['number'])
    print("Direccion + ciudad:",consulta['results'][0]['location']['city'])