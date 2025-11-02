import socket
import threading
from datetime import datetime

host = '127.0.0.1'
port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server berjalan di {}:{}".format(host, port))

clients = []
nicknames = []

def broadcast(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tagged = ('[' + timestamp + '] ').encode('ascii') + message
    for client in clients:
        client.send(tagged)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} keluar!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("Terhubung dengan {}".format(str(address)))
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Username {}".format(nickname))
        broadcast("{} Bergabung!".format(nickname).encode('ascii'))
        client.send('Terkoneksi dengan Server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()