# PERTEMUAN 3 - SOAL A

## Deskripsi
Program chat basic pake Python socket. Cuma bisa chat 1-on-1 aja sih, tapi lumayan buat belajar networking.

## Yang Ada di Sini

- `client.py` - Program client yang ngirim pesan
- `server.py` - Program server yang nerima pesan
- IP client auto-detect (kayaknya sih)

## Cara Pake

### 1. Jalankan Server Dulu
```bash
python server.py
```
Server bakal nunggu di port 12345

### 2. Jalankan Client
```bash
python client.py
```
Client bakal auto-detect IP-nya sendiri

### 3. Chat Aja
- Masukin IP server
- Masukin username
- Mulai chat

## Contoh Output

**Server:**
```
Alamat IP: 127.0.0.1
Masukkan Username: Yanto Kewer
Menerima koneksi dari 192.168.1.100
Budi sudah terhubung.
Budi : p mancengggg
```

**Client:**
```
Alamat IP Client: 192.168.1.100
Masukkan alamat IP Server: 127.0.0.1
Masukkan username: Yanto Kewer
Server Telah bergabung...
pesan : p mancengggg
```

## Yang Perlu Tau

- Pake Python 3
- Port 12345
- Cuma 1 client aja yang bisa connect
- IP client auto-detect pake Google DNS

## Kalau Error

- **Connection refused**: Server belum jalan
- **IP ga ke-detect**: Auto jadi 127.0.0.1
- **Port udah dipake**: Ganti port di kedua file

## Catatan

Ini cuma buat belajar aja. Kalau mau bikin chat beneran, perlu tambahin banyak fitur lagi.

Dibuat buat tugas PBJ Semester 3.
