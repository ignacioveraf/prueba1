import requests
import json

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    n=(input("ingrese un numero:"))
    dic = {"comentario" : consulta[int(n)]['body']}
    return dic
n=0
print(comment(n))