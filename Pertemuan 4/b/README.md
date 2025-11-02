# Folder B: Multi-Client Chat dengan Timestamp Jam

Yo! Folder B ini isinya multi-client chat server yang udah lengkap! Ada timestamp jam pada setiap pesan yang dikirim. Lebih rapi dan kayak chat beneran deh!

## Fitur

- **Multi-client support** - Banyak user bisa chat bareng  
- **Threading** - Handle multiple clients secara bersamaan  
- **Broadcasting** - Pesan dikirim ke semua user  
- **Timestamp Jam** (HH:MM:SS) - Setiap pesan ada waktu-nya  
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
Terhubung dengan IP 127.0.0.1:xxxxx
Telah terhubung dengan Username1
Terhubung dengan IP 127.0.0.1:xxxxx
Telah terhubung dengan Username2
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

Semua pesan bakal ter-broadcast ke semua user dengan timestamp jam. Misalnya:

```
[14:30:15] Alice: Halo semua!
[14:30:20] Bob: Hai Alice!
[14:30:25] Charlie: Apa kabar guys?
```

---

## Perbedaan dengan Folder A

| Feature | Folder A (Modul Contoh) | Folder B |
|---------|------------------------|----------|
| Timestamp | Tidak ada | Ada (HH:MM:SS) |
| Format Waktu | - | Jam:Menit:Detik |
| Informasi | Basic | Lebih informatif |
| User Experience | Simple | Lebih baik |

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
   → Server tambahkan timestamp [HH:MM:SS]
   → Broadcast ke semua client
6. Semua client terima pesan dengan timestamp
7. Client disconnect → remove dari list
   → Broadcast notif "Username keluar!"
```

---

## Code Highlights

### Timestamp Function
```python
def broadcast(message):
    timestamp = datetime.now().strftime('%H:%M:%S')  # Format: 14:30:15
    tagged = ('[' + timestamp + '] ').encode('ascii') + message
    for client in clients:
        client.send(tagged)
```

Simple tapi powerful! Setiap kali broadcast, otomatis tambah timestamp jam!

---

## Troubleshooting

**Problem**: "Address already in use"
- **Solution**: Ganti port number atau tutup aplikasi yang pakai port 5005

**Problem**: Client tidak terima pesan
- **Solution**: Pastikan server udah jalan dulu sebelum menjalankan client

**Problem**: Timestamp tidak muncul
- **Solution**: Check import datetime di server.py

---

## Future Enhancement Ideas

Bisa dikembangkan jadi:

1. **Private Message** - Tambahin fitur DM
2. **Room/Channel** - Buat multiple chat room
3. **File Sharing** - Kirim file/gambar
4. **User Authentication** - Login dengan password
5. **Message History** - Simpan chat ke database
6. **Rich Formatting** - Bold, italic, dll

---

## Happy Coding!

Chat server yang kayak beneran! Selamat eksplorasi dan jangan lupa develop fitur-fitur baru!
