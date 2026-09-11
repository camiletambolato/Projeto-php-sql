import json
from urllib.request import urlopen

cep = input("Digite o seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

with urlopen(url) as dados:
	resposta = json.load(dados)

print(f"Você mora na {resposta["logradouro"]} no bairro {resposta["bairro"]} em {resposta["localidade"]} localizado no estado de {resposta["estado"]}")
