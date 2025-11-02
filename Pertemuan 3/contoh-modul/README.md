# Contoh Modul: Basic Socket Programming

Welcome! Ini adalah modul contoh paling dasar untuk belajar socket programming. Perfect untuk pemula!

## Fitur

- Static port (12345)
- Static IP (127.0.0.1)
- One-way communication (client → server)
- Basic chat functionality

---

## Cara Menggunakan

### 1. Jalankan Server
```bash
python server.py
```

Server akan menanyakan username, lalu menunggu koneksi client.

Output:
```
Alamat IP: 127.0.0.1
Masukkan Username: Alice
```

### 2. Jalankan Client
```bash
python client.py
```

Client akan menanyakan:
- Alamat IP Server (ketik: 127.0.0.1)
- Username

Output:
```
Alamat IP Client: 127.0.0.1
Masukkan alamat IP Server: 127.0.0.1
Masukkan username: Bob
Bob Telah bergabung...
```

### 3. Mulai Chatting!

Di terminal client, ketik pesan:
```
pesan : Halo Alice!
pesan : Apa kabar?
```

Di terminal server, pesan akan muncul:
```
Bob : Halo Alice!
Bob : Apa kabar?
```

---

## Konsep Dasar yang Dipelajari

### 1. Socket Creation
Membuat socket TCP:
```python
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket = socket.socket()
```

### 2. Binding (Server)
Server "bind" ke IP dan port tertentu:
```python
serverSocket.bind(("127.0.0.1", 12345))
```

### 3. Listening (Server)
Server mendengarkan koneksi:
```python
serverSocket.listen()
```

### 4. Accepting Connection (Server)
Server menerima koneksi dari client:
```python
msg, addrs = serverSocket.accept()
```

### 5. Connecting (Client)
Client connect ke server:
```python
clientSocket.connect(("127.0.0.1", 12345))
```

### 6. Send & Receive
Cara mengirim dan menerima data:
```python
# Mengirim data (encode ke bytes)
clientSocket.send(name.encode())

# Menerima data (decode ke string)
message = msg.recv(1024).decode()
```

---

## Alur Kerja

```
1. Server start
   ↓
2. Server bind ke 127.0.0.1:12345
   ↓
3. Server listen() untuk koneksi
   ↓
4. Client start dan connect ke server
   ↓
5. Server accept() koneksi client
   ↓
6. Pertukaran username:
   - Client kirim username → Server terima
   - Server kirim username → Client terima
   ↓
7. Chat dimulai:
   - Client kirim pesan
   - Server terima dan tampilkan
   (hanya satu arah: client ke server)
```

---

## Keterbatasan

- Port tetap (tidak bisa diubah)
- IP statis (harus pakai 127.0.0.1)
- One-way communication (server tidak bisa balas)
- Hanya 1 client bisa connect

---

## Next Steps

Setelah paham modul ini, tingkatkan ke:
- **Folder A**: Auto-detect IP client
- **Folder B**: Dynamic port configuration
- **Folder C**: Tambah timestamp
- **Folder E**: Two-way communication

---

## Troubleshooting

**Problem**: "Address already in use"
- **Solution**: Tutup aplikasi lain yang pakai port 12345, atau tunggu beberapa saat

**Problem**: Can't connect
- **Solution**: Pastikan server sudah jalan dulu, pastikan IP: 127.0.0.1

**Problem**: Pesan tidak muncul di server
- **Solution**: Pastikan server udah jalan dan sudah accept client

---

## Tips Belajar

1. Run server dulu, baru run client
2. Perhatikan error message dengan teliti
3. Coba ganti-ganti username dan pesan
4. Coba tutup salah satu terminal dan lihat apa yang terjadi
5. Read the code line by line, pahami setiap baris

---

## Happy Coding!

Ini adalah langkah pertama kamu di socket programming! Jangan lupa practice dan experiment!

