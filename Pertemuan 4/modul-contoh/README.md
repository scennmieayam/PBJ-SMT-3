# Modul Contoh: Basic Multi-Client Chat Server

Welcome ke modul contoh! Ini adalah **fondasi dasar** untuk multi-client chat server. Perfect untuk pemula yang baru belajar socket programming dengan threading!

## Fitur

- **Multi-client support** - Banyak user bisa chat bareng  
- **Threading** - Handle multiple clients secara bersamaan  
- **Broadcasting** - Pesan dikirim ke semua user  
- **Auto-disconnect** - Handle disconnect dengan benar  
- **Join notifications** - Notifikasi ketika ada yang join  

---

## Cara Menggunakan

### 1. Jalankan Server
```bash
python server.py
```

Output:
```
Terhubung dengan ('127.0.0.1', xxxxx)
Username Alice
Terhubung dengan ('127.0.0.1', xxxxx)
Username Bob
```

### 2. Jalankan Client (Multiple Terminal)

Buka terminal baru untuk setiap client:

```bash
# Terminal 2
python client.py
Masukkan username: Alice
>> 

# Terminal 3
python client.py
Masukkan username: Bob
>> 

# Terminal 4
python client.py
Masukkan username: Charlie
>> 
```

### 3. Mulai Chatting!

Semua pesan bakal ter-broadcast ke semua user. Misalnya:

```
Alice: Halo semua!
Bob: Hai Alice!
Charlie: Apa kabar guys?
```

---

## Konsep Dasar yang Dipelajari

### 1. **Threading**
Setiap client yang connect dapat **thread sendiri**, jadi tidak block thread lain!

```python
thread = threading.Thread(target=handle, args=(client,))
thread.start()
```

**Kenapa penting?**
- Multiple clients bisa connect bersamaan
- Satu client tidak block client lain
- Server bisa handle banyak koneksi sekaligus

### 2. **Broadcasting**
Pesan dari satu client dikirim ke **semua client** yang terhubung!

```python
def broadcast(message):
    for client in clients:
        client.send(message)
```

**Flow:**
```
Client A kirim "Hello"
    ↓
Server terima pesan
    ↓
broadcast() kirim ke semua client di list
    ↓
Client A, B, C, D... semua terima "Hello"
```

### 3. **List Management**
Manage semua client yang terhubung dengan list!

```python
clients = []      # Simpan socket client
nicknames = []    # Simpan username
```

**CRUD Operations:**
- **Create**: Tambah client baru ketika connect
- **Read**: Loop through clients untuk broadcast
- **Update**: Update list ketika ada yang keluar
- **Delete**: Remove client dari list

---

## Alur Kerja Lengkap

```
1. Server Start
   ↓
2. Server listen() untuk koneksi baru
   ↓
3. Client 1 Connect
   → Server accept() koneksi
   → Minta username dengan 'NICK'
   → Terima username dan simpan ke nicknames[]
   → Simpan client socket ke clients[]
   → Buat thread baru untuk handle Client 1
   → Broadcast "Client 1 Bergabung!"
   ↓
4. Client 2, 3, 4... Connect (sama seperti Client 1)
   ↓
5. Client 1 kirim pesan "Hello"
   → Thread Client 1 terima pesan
   → broadcast() kirim ke semua client di clients[]
   → Semua client terima "Hello"
   ↓
6. Client 2 kirim pesan "Hi"
   → Thread Client 2 terima pesan
   → broadcast() kirim ke semua client
   → Semua client terima "Hi"
   ↓
7. Client 1 disconnect
   → Exception terjadi di thread Client 1
   → Remove Client 1 dari clients[] dan nicknames[]
   → Close socket Client 1
   → Broadcast "Client 1 keluar!"
   → Thread Client 1 selesai
```

---

## Materi Pembelajaran

### Import yang Digunakan
```python
import socket      # Untuk network communication
import threading   # Untuk handle multiple clients
```

### Function Penting

#### 1. `broadcast(message)`
Kirim pesan ke **semua client** yang terhubung
```python
def broadcast(message):
    for client in clients:
        client.send(message)
```

#### 2. `handle(client)`
Handle pesan dari **satu client** tertentu
```python
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Handle disconnect
            remove_client(client)
```

#### 3. `receive()`
Terima koneksi **client baru**
```python
def receive():
    while True:
        client, address = server.accept()
        # Setup client baru
        # Buat thread baru
```

### Thread Model
```
Main Thread (receive)
  ├── Thread 1 (handle Client A)
  ├── Thread 2 (handle Client B)
  ├── Thread 3 (handle Client C)
  └── ...
```

Setiap thread bekerja **independen**, tidak saling ganggu!

---

## Konfigurasi

### Mengubah Port
Edit di `server.py` dan `client.py`:

```python
# server.py
port = 5005  # Ganti port di sini

# client.py
client.connect(('127.0.0.1', 5005))  # Ganti port di sini
```

### Mengubah Host
Edit di `server.py` dan `client.py`:

```python
# server.py
host = '127.0.0.1'  # Ganti host di sini

# client.py
client.connect(('127.0.0.1', 5005))  # Ganti host di sini
```

---

## Troubleshooting

### Problem 1: "Address already in use"
**Penyebab**: Port masih dipakai aplikasi lain

**Solution**: 
```bash
# Linux/Mac
lsof -i :5005
kill -9 <PID>

# Atau ganti port number
```

### Problem 2: Client tidak terima pesan
**Penyebab**: Server belum jalan atau broadcasting tidak bekerja

**Solution**: 
- Pastikan server udah jalan dulu
- Check fungsi broadcast() benar
- Check client list tidak kosong

### Problem 3: Multiple clients tidak bisa connect
**Penyebab**: Threading tidak bekerja dengan benar

**Solution**: 
- Pastikan import threading
- Check thread.start() dipanggil
- Pastikan tidak ada blocking code

### Problem 4: Server crash ketika client disconnect
**Penyebab**: Exception handling tidak proper

**Solution**: 
- Pastikan ada try-except di handle()
- Check index management saat remove client
- Close socket dengan benar

---

## Perbedaan dengan Pertemuan 3

| Feature | Pertemuan 3 | Modul Contoh (Pertemuan 4) |
|---------|-------------|----------------------------|
| Client Support | 1 client saja | Multiple clients |
| Threading | Tidak pakai | Pakai threading |
| Broadcasting | Tidak ada | Ada |
| List Management | Tidak perlu | Perlu manage list |
| Kompleksitas | Simple | Advanced |

**Upgrade dari Pertemuan 3:**
- Bisa handle **banyak client** sekaligus
- Menggunakan **threading** untuk concurrency
- **Broadcasting** pesan ke semua user

---

## Exercises / Challenges

Coba challenge berikut untuk mengasah skill:

1. **Tambah Timestamp** (Lihat Folder A & B!)
   - Tambah timestamp pada setiap pesan
   - Format: [HH:MM:SS] atau [YYYY-MM-DD HH:MM:SS]

2. **Validasi Username**
   - Username tidak boleh kosong
   - Username tidak boleh sama

3. **Private Message**
   - Command: `/pm username message`
   - Kirim pesan ke user tertentu saja

4. **Admin Commands**
   - `/kick username` - kick user dari chat
   - `/list` - list semua user online

---

## Next Steps

Setelah paham modul contoh ini, lanjut ke:

1. **Folder A** - Tambah timestamp lengkap (date + time)
2. **Folder B** - Tambah timestamp jam saja (time)
3. **Custom Project** - Buat fitur sendiri!

---

## Tips Belajar

1. **Tidak ada "dumb question"** - Tanya semua yang belum paham!
2. **Break down masalah** - Pecah jadi bagian kecil
3. **Read error messages** - Pelajari error message dengan teliti
4. **Practice makes perfect** - Latihan coding sesering mungkin
5. **Experiment** - Coba ubah kode dan lihat hasilnya!

---

## Happy Coding!

Selamat! Kamu udah paham dasar multi-client chat server! Ini adalah langkah besar untuk menjadi socket programming expert!

**Jangan lupa**: Explore, experiment, dan have fun!
