# Penjelasan Perubahan Kode antara modul-contoh dan folder a

## Deskripsi Perubahan

Pada percobaan ini, dilakukan modifikasi pada sisi server untuk menambahkan fitur timestamp pada setiap pesan yang dikirim ke klien. Modifikasi dilakukan dengan mengimpor modul `datetime` yang digunakan untuk mengambil waktu saat pesan dikirim. Fungsi `broadcast()` kemudian dimodifikasi untuk menambahkan timestamp pada setiap pesan dalam format `[YYYY-MM-DD HH:MM:SS]` sebelum pesan tersebut dikirim ke semua klien yang terhubung. Selain itu, ditambahkan juga pesan informasi saat server berjalan yang menampilkan alamat IP dan port yang digunakan server, sehingga administrator dapat mengetahui status server dengan jelas. Setiap pesan yang diterima oleh klien akan secara otomatis diawali dengan timestamp yang menunjukkan kapan pesan tersebut dikirim, memungkinkan pelacakan waktu pengiriman pesan dalam sistem chat. Sementara itu, file client.py tidak mengalami perubahan sama sekali dan tetap berfungsi seperti sebelumnya, hanya menerima pesan yang sudah ditandai timestamp oleh server.

## Ringkasan Perubahan

Setelah membandingkan kode antara folder `modul-contoh` dan folder `a`, ditemukan bahwa:

- **client.py**: **TIDAK ADA PERUBAHAN** - kedua file identik
- **server.py**: **ADA PERUBAHAN** - terdapat 3 perubahan utama

---

## Detail Perubahan pada server.py

### 1. Penambahan Import Module `datetime`

**Lokasi**: Baris 3

**Sebelum** (modul-contoh):
```python
import socket
import threading
```

**Sesudah** (folder a):
```python
import socket
import threading
from datetime import datetime
```

**Penjelasan**: 
- Ditambahkan import `datetime` untuk menampilkan timestamp pada setiap pesan yang dikirim ke semua klien.

---

### 2. Penambahan Pesan Informasi Server Berjalan

**Lokasi**: Baris 12 (setelah `server.listen()`)

**Sebelum** (modul-contoh):
```python
server.listen()

clients = []
```

**Sesudah** (folder a):
```python
server.listen()

print("Server berjalan di {}:{}".format(host, port))

clients = []
```

**Penjelasan**: 
- Ditambahkan print statement untuk menampilkan informasi bahwa server telah berjalan beserta alamat IP dan port yang digunakan.
- Ini membantu administrator server mengetahui status server saat startup.
- Output: `Server berjalan di 127.0.0.1:5005`

---

### 3. Modifikasi Fungsi `broadcast()` untuk Menambahkan Timestamp

**Lokasi**: Fungsi `broadcast()` (baris 17-21)

**Sebelum** (modul-contoh):
```python
def broadcast(message):
    for client in clients:
        client.send(message)
```

**Sesudah** (folder a):
```python
def broadcast(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tagged = ('[' + timestamp + '] ').encode('ascii') + message
    for client in clients:
        client.send(tagged)
```

**Penjelasan**: 
- Fungsi `broadcast()` dimodifikasi untuk menambahkan timestamp pada setiap pesan yang dikirim.
- Format timestamp: `YYYY-MM-DD HH:MM:SS` (contoh: `2024-01-15 14:30:25`)
- Setiap pesan yang diterima klien akan diawali dengan timestamp dalam format `[2024-01-15 14:30:25] pesan asli`
- Ini membantu tracking waktu kapan pesan dikirim dalam sistem chat.

**Contoh Output Pesan**:
- **Sebelum**: `John: Hello everyone!`
- **Sesudah**: `[2024-01-15 14:30:25] John: Hello everyone!`

---

## Manfaat Perubahan

1. **Traceability**: Dengan timestamp, dapat melacak kapan setiap pesan dikirim
2. **Monitoring**: Pesan startup membantu memastikan server berjalan dengan benar
3. **Debugging**: Timestamp memudahkan troubleshooting jika terjadi masalah

---

## Catatan Penting

- **client.py tidak berubah**: Klien tetap berfungsi seperti sebelumnya, hanya menerima pesan yang sudah ditandai timestamp oleh server
- **Kompatibilitas**: Perubahan ini **backward compatible** - klien lama masih bisa terhubung ke server baru, hanya saja pesan yang diterima akan memiliki format timestamp baru

