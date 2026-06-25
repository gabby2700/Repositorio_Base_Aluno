#Biblioteca requests
"""
Biblioteca Python que permite secomunicar com o protocolo HTTP de forma 
fácil e intuitiva.

-Requisição 
--Cabeçalhos
--Corpo

-Resposta
--Status
--Cabeçalho
--Corpo 
"""

import requests

cep = input("Digite o cep que deseja consultar:")

resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")


if resposta.status_code == 200:
    dados = resposta.json()
    print(dados.get("address"))
    print(f"{dados.get("city")} — {dados.get("state")}")
else:
    print("CEP inválide, verifique o CEP e tente novamente.")