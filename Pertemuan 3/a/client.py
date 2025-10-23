import socket

# Fungsi untuk mendapatkan IP client secara otomatis (TAMBAHAN DARI CONTOH MODUL)
def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return "127.0.0.1"

clientSocket = socket.socket()
# Menggunakan fungsi get_local_ip() untuk mendapatkan IP otomatis (DIUBAH DARI CONTOH MODUL)
client_ip = get_local_ip()
# Menampilkan IP client yang didapat secara otomatis (DIUBAH DARI CONTOH MODUL)
print(f'Alamat IP Client: {client_ip}')
server_host = input('Masukkan alamat IP Server: ')
name = input('Masukkan username: ')
clientSocket.connect((server_host, 5007))

clientSocket.send(name.encode())
server_name = clientSocket.recv(1024)
server_name = server_name.decode()

print(server_name,' Telah bergabung...')
while True:
    message = input("pesan : ")
    clientSocket.send(message.encode())