import socket
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#input port server secara dinamis
server_port = int(input('Masukkan Port Server: '))
serverSocket.bind(("127.0.0.1", server_port))

print("Alamat IP: 127.0.0.1")
print(f"Port Server: {server_port}")
#menampilkan tanggal diawal
print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d')}")
name = input('Masukkan Username: ')
serverSocket.listen()

msg, addrs = serverSocket.accept()
print("Menerima koneksi dari ", addrs[0])
print('Terkoneksi dari: ',addrs[0])

client = (msg.recv(1024)).decode()
print(client + ' sudah terhubung.')
msg.send(name.encode())

while True:
    message = msg.recv(1024)
    message = message.decode()
    #menampilkan waktu pada setiap pesan dari client
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"[{current_time}] {client}: {message}")
    
    #input pesan dari server untuk dikirim ke client (TAMBAHAN DARI CONTOH MODUL)
    server_message = input(f"[{name}] pesan: ")
    #mengirim pesan server dengan timestamp ke client (TAMBAHAN DARI CONTOH MODUL)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg.send(f"[{timestamp}] {name}: {server_message}".encode())