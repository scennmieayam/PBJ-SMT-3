# Pertemuan 3: Socket Programming Basics

Mantap! Di pertemuan ini kita belajar tentang **socket programming** yang merupakan dasar untuk membuat aplikasi **client-server**. Kita akan belajar komunikasi antar aplikasi menggunakan TCP socket!

## Struktur Folder

```
Pertemuan 3/
├── a/          # Basic socket (one-way communication)
├── b/          # Dynamic port configuration
├── c/          # Timestamp pada pesan
├── e/          # Two-way communication + timestamp
└── contoh-modul/ # Materi dasar socket programming
```

---

## Materi Pembelajaran

### 1. **Contoh Modul** (`contoh-modul/`)
**Level**: Pemula

Ini adalah contoh paling dasar! Server dan client bisa chat, tapi cuma **server yang bisa nerima pesan**, client cuma bisa kirim.

**Cara Pakai:**
1. Buka terminal 1 → jalankan `python server.py`
2. Buka terminal 2 → jalankan `python client.py`
3. Chat deh!

**Fitur:**
- Port statis (12345)
- IP statis (127.0.0.1)
- One-way communication

---

### 2. **Folder A** (`a/`)
**Level**: Pemula

Sama kayak contoh modul, tapi udah dikasih **IP client detection otomatis**! Jagoan dikit lah ya

**Cara Pakai:**
```bash
# Terminal 1 (Server)
python server.py

# Terminal 2 (Client)
python client.py
```

**Fitur:**
- IP client auto-detect
- Port statis (5007)
- One-way communication

---

### 3. **Folder B** (`b/`)
**Level**: Intermediet

Nah ini lebih keren! Port bisa **custom**, jadi fleksibel lah. Misalnya mau pakai port 8080? Bisa!

**Cara Pakai:**
```bash
# Terminal 1 (Server)
python server.py
# Masukkan port (misal: 5005)

# Terminal 2 (Client)
python client.py
# Masukkan IP Server & Port Server
```

**Fitur:**
- Dynamic port configuration
- IP client auto-detect
- One-way communication

---

### 4. **Folder C** (`c/`)
**Level**: Intermediet

Tambahin **tanggal dan waktu** biar kayak chat beneran! Setiap pesan yang masuk bakal ketimestamp.

**Cara Pakai:**
```bash
# Terminal 1 (Server)
python server.py
# Tanggal bakal muncul otomatis!

# Terminal 2 (Client)
python client.py
# Pesan otomatis ke-capture timestamp-nya!
```

**Fitur:**
- Dynamic port configuration
- IP client auto-detect
- Timestamp pada setiap pesan
- One-way communication

---

### 5. **Folder E** (`e/`)
**Level**: Advanced

Yang paling lengkap nih! **Two-way communication** + **timestamp**. Server bisa balas pesan, client juga bisa nerima balasan. Kayak WhatsApp lah pokoknya! 

**Cara Pakai:**
```bash
# Terminal 1 (Server)
python server.py

# Terminal 2 (Client)
python client.py

# Sekarang bisa chat dua arah!
```

**Fitur:**
- Dynamic port configuration
- IP client auto-detect
- Timestamp pada setiap pesan
- **Two-way communication** (server bisa balas!)
- Timestamp format lengkap (tanggal + waktu)

---

## Teknologi yang Digunakan

- **Python 3.x**
- **Socket Library** (built-in)
- **Datetime** (untuk timestamp)

---

## Konsep Penting

1. **Socket**: Jalur komunikasi antara dua program
2. **TCP**: Protocol yang reliable untuk komunikasi
3. **Binding**: Server "bind" ke IP dan port tertentu
4. **Connect**: Client "connect" ke server
5. **Send/Receive**: Cara kirim terima data
6. **Threading**: (Pertemuan 4) untuk handle multiple clients

---

## Troubleshooting

**Error "Address already in use"?**
- Ganti port number-nya atau tutup aplikasi yang pakai port yang sama

**Can't connect?**
- Pastikan IP server-nya bener
- Pastikan port-nya sama antara server dan client

**Pesan tidak muncul?**
- Pastikan server udah jalan dulu sebelum jalankan client

---

## Catatan Penting

- **Selalu jalankan server dulu** sebelum client!
- Kalau pakai `127.0.0.1` atau `localhost`, berarti testing di **satu komputer** yang sama
- Untuk testing di komputer berbeda, pakai **IP address lokal** (biasanya 192.168.x.x)
- Port yang digunakan harus **unique** dan tidak conflict dengan aplikasi lain

---

## Happy Coding!

Jangan lupa explore dan coba-coba sendiri ya! Semakin sering latihan, semakin jago!

**Next Level**: Pertemuan 4 - Multi-client Chat Server!
