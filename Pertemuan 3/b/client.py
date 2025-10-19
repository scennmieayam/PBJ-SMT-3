import socket

def getClientIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

clientSocket = socket.socket()
client_ip = getClientIP()
print(f'Alamat IP Client: {client_ip}')
server_host = input('Masukkan alamat IP Server: ')
name = input('Masukkan username: ')

clientSocket.connect((server_host, 12345))
clientSocket.send(name.encode())

server_name = clientSocket.recv(1024).decode()
print(server_name, 'Telah bergabung...')

while True:
    message = input("pesan : ")
    clientSocket.send(message.encode())