import requests

cep: str = str(input('digite o CEP: '))

url = f'https://cep.awesomeapi.com.br/json/{cep}'

# Tratando possiveis erros
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print(f'Erro HTTP: {errh}')
except requests.exceptions.ConnectionError as errc:
    print(f'Erro de conexão: {errc}')
except requests.exceptions.Timeout as time:
    print(f'Erro de timeout: {time}')
except requests.exceptions.RequestException as err:
    print(f'Erro desconhecido: {err}')
else: # executa programa
    if response.status_code == 200:
        try: 
            data = response.json()
            print(f"Endereço: {data['address']}")
            print(f"Cidade: {data['city']}, {data['state']}")
            print(f"DDD: {data['ddd']}")
        except:
            print('Houve algum Erro')
    else:
        print('CEP não encontrado...')
