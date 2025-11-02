# Folder A: Multi-Client Chat dengan Timestamp Lengkap

Wah! Folder A ini versi paling lengkap! Multi-client chat server dengan **timestamp lengkap** yang menampilkan tanggal dan waktu. Perfect untuk tracking history chat!

## Fitur

- **Multi-client support** - Banyak user bisa chat bareng  
- **Threading** - Handle multiple clients secara bersamaan  
- **Broadcasting** - Pesan dikirim ke semua user  
- **Timestamp Lengkap** (YYYY-MM-DD HH:MM:SS) - Tanggal + waktu detail!
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
Server berjalan di 127.0.0.1:5005
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

Semua pesan bakal ter-broadcast ke semua user dengan timestamp lengkap. Misalnya:

```
[2024-01-15 14:30:15] Alice: Halo semua!
[2024-01-15 14:30:20] Bob: Hai Alice!
[2024-01-15 14:30:25] Charlie: Apa kabar guys?
```

---

## Perbedaan dengan Folder Lainnya

| Feature | Modul Contoh | Folder A | Folder B |
|---------|-------------|----------|----------|
| Timestamp | Tidak ada | Lengkap (date + time) | Jam saja |
| Format | - | YYYY-MM-DD HH:MM:SS | HH:MM:SS |
| Informasi | Basic | Lengkap detail | Compact |
| Use Case | Simple chat | Professional chat | Quick chat |

**Kenapa Pilih Folder A?**
- Perlu tracking **tanggal** juga, bukan cuma waktu
- Ingin format timestamp yang **lengkap dan jelas**
- Cocok untuk aplikasi yang butuh **audit trail**

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

## Alur Kerja

```
1. Server start → listen di port 5005
2. Client connect → kirim username
3. Server terima username → simpan ke list
4. Server buat thread baru untuk client
5. Client A kirim pesan
   → Server tambahkan timestamp lengkap [YYYY-MM-DD HH:MM:SS]
   → Broadcast ke semua client
6. Semua client terima pesan dengan timestamp
7. Client disconnect → remove dari list
   → Broadcast notif "Username keluar!"
```

---

## Code Highlights

### Timestamp Lengkap Function
```python
def broadcast(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Format: 2024-01-15 14:30:15
    tagged = ('[' + timestamp + '] ').encode('ascii') + message
    for client in clients:
        client.send(tagged)
```

Format lengkap memberikan konteks waktu **penuh**: tanggal, bulan, tahun, jam, menit, dan detik!

---

## Troubleshooting

**Problem**: "Address already in use"
- **Solution**: Ganti port number atau tutup aplikasi yang pakai port 5005

**Problem**: Client tidak terima pesan
- **Solution**: Pastikan server udah jalan dulu sebelum menjalankan client

**Problem**: Timestamp tidak muncul
- **Solution**: Check import datetime di server.py

**Problem**: Format tanggal aneh
- **Solution**: Check sistem tanggal di komputer kamu sudah benar

---

## Perbandingan Timestamp

### Folder A (Timestamp Lengkap)
```
[2024-01-15 14:30:15] User: Message
```
- Lengkap dan jelas  
- Bisa tracking history  
- Professional look  
- Lebih panjang  

### Folder B (Timestamp Jam Saja)
```
[14:30:15] User: Message
```
- Lebih compact  
- Tidak makan space  
- Simple dan clean  
- Tidak ada tanggal  

**Kesimpulan**: Pilih sesuai kebutuhan! Folder A untuk aplikasi yang perlu **tracking detail**, Folder B untuk chat **real-time** yang simple!

---

## Future Enhancement Ideas

Bisa dikembangkan jadi:

1. **Database Logging** - Simpan chat dengan timestamp ke database
2. **Search by Date** - Cari chat berdasarkan tanggal
3. **Export Chat History** - Export chat dengan format CSV/JSON
4. **Time-based Commands** - Fitur seperti "show messages from yesterday"
5. **Timezone Support** - Support multiple timezone

---

## Happy Coding!

Chat server dengan timestamp lengkap yang kayak aplikasi professional! Semoga bermanfaat untuk project kamu!
