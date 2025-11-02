# Folder C: Socket dengan Timestamp

Folder C adalah upgrade dari Folder B dengan penambahan **timestamp pada setiap pesan**. Sekarang server menampilkan waktu pada setiap pesan yang diterima dari client!

## Fitur

- Dynamic port configuration
- IP client auto-detect
- Timestamp pada setiap pesan (HH:MM:SS)
- Tanggal ditampilkan di awal
- One-way communication

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
```

### 3. Mulai Chatting!

Setiap pesan dari client akan ditampilkan dengan timestamp:

Server Output:
```
[14:30:15] Bob: Halo Alice!
[14:30:25] Bob: Apa kabar?
```

---

## Konsep yang Dipelajari

### 1. Timestamp pada Pesan
Server menambahkan waktu pada setiap pesan yang diterima:
```python
current_time = datetime.now().strftime('%H:%M:%S')
print(f"[{current_time}] {client}: {message}")
```

Format timestamp: HH:MM:SS (Jam:Menit:Detik)

### 2. Tanggal di Awal
Server menampilkan tanggal saat pertama kali dimulai:
```python
print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d')}")
```

---

## Perbedaan dengan Folder Lain

| Feature | Folder A | Folder B | Folder C | Folder E |
|---------|----------|----------|----------|----------|
| Static Port | ✓ | ✗ | ✗ | ✗ |
| Dynamic Port | ✗ | ✓ | ✓ | ✓ |
| IP Auto-detect | ✓ | ✓ | ✓ | ✓ |
| Timestamp | ✗ | ✗ | ✓ | ✓ |
| Two-way Chat | ✗ | ✗ | ✗ | ✓ |

---

## Konfigurasi

### Mengubah Format Timestamp

Edit di `server.py`:
```python
# Format saat ini: HH:MM:SS
current_time = datetime.now().strftime('%H:%M:%S')

# Bisa diubah menjadi format lain:
# current_time = datetime.now().strftime('%I:%M:%S %p')  # 12-hour format
# current_time = datetime.now().strftime('%H:%M')        # Tanpa detik
```

### Mengubah Format Tanggal

Edit di `server.py`:
```python
# Format saat ini: YYYY-MM-DD
print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d')}")

# Bisa diubah menjadi format lain:
# datetime.now().strftime('%d/%m/%Y')  # DD/MM/YYYY
# datetime.now().strftime('%d-%B-%Y')  # DD-Month-YYYY
```

---

## Troubleshooting

**Problem**: Timestamp tidak muncul
- **Solution**: Pastikan import datetime ada di server.py

**Problem**: Format waktu aneh
- **Solution**: Check sistem waktu komputer sudah benar

**Problem**: Port sudah dipakai
- **Solution**: Pilih port lain atau tutup aplikasi yang menggunakan port tersebut

**Problem**: Koneksi gagal
- **Solution**: Pastikan IP dan port server sama dengan yang diisi di client

---

## Next Level

Setelah memahami folder ini, kamu bisa lanjut ke:
- **Folder E**: Two-way communication dengan timestamp

---

## Happy Coding!

Sekarang pesan chat punya timestamp! Lebih profesional dan mudah tracking waktu pesan!

