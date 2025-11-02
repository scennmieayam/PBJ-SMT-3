# Folder E: Two-Way Communication dengan Timestamp

Folder E adalah versi paling lengkap dan canggih! Ini menggabungkan semua fitur sebelumnya PLUS **two-way communication**. Server bisa balas pesan client, dan client juga bisa nerima pesan server. Seperti WhatsApp!

## Fitur

- Dynamic port configuration
- IP client auto-detect
- Timestamp pada setiap pesan (dua format berbeda!)
- Tanggal ditampilkan di awal
- **Two-way communication** (Server bisa balas!)
- Format timestamp lengkap pada pesan server

---

## Cara Menggunakan

### 1. Jalankan Server
```bash
python server.py
```

Server akan meminta:
- Port Server (contoh: 5005)
- Username

Output:
```
Alamat IP: 127.0.0.1
Port Server: 5005
Tanggal: 2024-01-15
Masukkan Username: Alice
```

### 2. Jalankan Client
```bash
python client.py
```

Client akan menampilkan IP-nya dan meminta:
- Alamat IP Server (contoh: 127.0.0.1)
- Port Server (harus sama dengan server)
- Username

Output:
```
Alamat IP Client: 127.0.0.1
Masukkan alamat IP Server: 127.0.0.1
Masukkan Port Server: 5005
Masukkan username: Bob
Alice Telah bergabung...
```

### 3. Mulai Chatting!

Client kirim pesan:
```
pesan : Halo Alice!
```

Server akan tampilkan:
```
[14:30:15] Bob: Halo Alice!
[Alice] pesan: _
```

Server bisa balas:
```
[Alice] pesan: Halo juga Bob!
```

Client akan terima:
```
[2024-01-15 14:30:20] Alice: Halo juga Bob!
```

---

## Konsep yang Dipelajari

### 1. Two-Way Communication
Baik server maupun client bisa kirim dan terima pesan:

**Server Side:**
```python
# Terima pesan dari client
message = msg.recv(1024)
message = message.decode()

# Kirim pesan ke client
server_message = input(f"[{name}] pesan: ")
msg.send(f"[{timestamp}] {name}: {server_message}".encode())
```

**Client Side:**
```python
# Kirim pesan ke server
message = input("pesan : ")
clientSocket.send(message.encode())

# Terima pesan dari server
server_response = clientSocket.recv(1024)
server_response = server_response.decode()
print(server_response)
```

### 2. Dua Format Timestamp

**Di Server** (untuk pesan dari client):
```python
current_time = datetime.now().strftime('%H:%M:%S')
print(f"[{current_time}] {client}: {message}")
# Output: [14:30:15] Bob: Hello
```

**Di Client** (untuk pesan dari server):
```python
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
msg.send(f"[{timestamp}] {name}: {server_message}".encode())
# Output: [2024-01-15 14:30:20] Alice: Hi!
```

Format berbeda memberikan informasi yang lebih lengkap!

---

## Perbedaan dengan Folder Lain

| Feature | Folder C | Folder E |
|---------|----------|----------|
| Dynamic Port | ✓ | ✓ |
| IP Auto-detect | ✓ | ✓ |
| Timestamp | ✓ | ✓ |
| Tanggal di Awal | ✓ | ✓ |
| Two-way Chat | ✗ | ✓ |
| Server Bisa Balas | ✗ | ✓ |

---

## Alur Komunikasi

```
1. Server start dan listen
2. Client connect ke server
3. Pertukaran username
4. Chat dimulai:
   
   CLIENT SIDE:
   - Client ketik pesan → kirim ke server
   - Client tunggu response → terima dari server
   
   SERVER SIDE:
   - Server terima pesan dari client → tampilkan
   - Server ketik balasan → kirim ke client
   
5. Proses berulang (dua arah!)
```

---

## Tips Menggunakan

1. **Balance**: Setelah kirim pesan, tunggu response sebelum kirim lagi
2. **Read Carefully**: Perhatikan format timestamp yang berbeda
3. **Take Turns**: Chat lebih smooth kalau bergantian
4. **Practice**: Coba berbagai skenario percakapan

---

## Troubleshooting

**Problem**: Server atau client stuck
- **Solution**: Pastikan setelah kirim pesan, tunggu terima dulu baru kirim lagi

**Problem**: Pesan tidak muncul
- **Solution**: Check apakah ada input dari pihak lain terlebih dahulu

**Problem**: Timestamp tidak konsisten
- **Solution**: Ini normal! Timestamp di server dan client formatnya berbeda

**Problem**: Port sudah dipakai
- **Solution**: Pilih port lain atau tutup aplikasi yang menggunakan port tersebut

---

## Keunggulan Folder E

- Fitur paling lengkap di Pertemuan 3
- Two-way communication untuk chat real-time
- Timestamp lengkap untuk tracking
- Flexible dengan dynamic port
- Auto-detect IP untuk kemudahan

---

## Next Level

Setelah mahir folder ini, kamu siap untuk:
- **Pertemuan 4**: Multi-client server dengan threading!

---

## Happy Coding!

Selamat! Kamu sudah menguasai socket programming dasar yang lengkap! Ini adalah foundation yang solid untuk belajar advanced socket programming!

