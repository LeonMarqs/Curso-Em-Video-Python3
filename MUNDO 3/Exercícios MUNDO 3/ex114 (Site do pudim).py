import requests
from requests.exceptions import ConnectionError
try:
    response = requests.get('http://www.pudim.com.br')

except ConnectionError:
    print('\033[31mNão consegui entrar no site\033[m')
else:
    print('\033[33mConsegui entrar no site do pudim\033[m')