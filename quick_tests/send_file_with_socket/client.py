import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('', 5001))

while True:
    response = client.recv(1024)
    print(response)
    if not response:
        break

print('acabou pae')
# with open(response.get('file_name'), 'w') as f:
#     f.write(response['data'])
