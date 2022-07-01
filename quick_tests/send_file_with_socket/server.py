import requests
import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 5001))
server.listen(5)

while True:
    response = requests.get('https://source.unsplash.com/random/')
    print('Aguardando nova conexão...')
    client_socket, addr = server.accept()
    client_socket.send(response.content)
    print('Imagem enviada')

