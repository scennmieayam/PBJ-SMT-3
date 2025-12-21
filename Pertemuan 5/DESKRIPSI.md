# Deskripsi Pengerjaan Landing Page Web Profil Roblox

## 1. Buatlah Landing Page untuk Web Profil Statis dengan Memanfaatkan Assets Online

### Yang Telah Dilakukan:

**Struktur HTML:**
- Membuat struktur landing page dengan HTML5 semantik
- Menggunakan Bootstrap 3.4.1 untuk framework responsif
- Membuat 5 section utama:
  - **Beranda (Home)**: Section pembuka dengan logo Roblox
  - **Tentang (About)**: Informasi tentang platform Roblox
  - **Permainan (Games)**: Menampilkan 3 game populer
  - **Galeri (Gallery)**: Menampilkan 4 gambar gallery
  - **Footer**: Informasi copyright

**Pemanfaatan Assets Online:**
- **Logo Roblox**: Menggunakan gambar dari Wikipedia Commons
  - URL: `https://upload.wikimedia.org/wikipedia/commons/1/1e/Roblox_Logo_2025.png`
  
- **Gambar About**: Menggunakan gambar dari Google Images
  - URL: `https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVjcRCq4kpZ2spSTDReL50zz9Ug7OQmEiEmw&s`
  
- **Gambar Game:**
  - Adopt Me: `https://thumb.viva.id/vivadigital/1265x711/2025/06/20/685522993683f-adopt-me-roblox_digital.jpg`
  - Fishit: `https://tr.rbxcdn.com/180DAY-600081d81c133f2c6dc8bb52522f2845/768/432/Image/Webp/noFilter`
  - Brookhaven: `https://tr.rbxcdn.com/180DAY-808370c4e617d8ce593b16f54eaf645d/768/432/Image/Webp/noFilter`
  
- **Gambar Gallery**: Menggunakan 4 gambar berbeda dari Unsplash
  - Gallery 1: `https://images.unsplash.com/photo-1566577134770-3d85bb3a9cc4?w=300`
  - Gallery 2: `https://images.unsplash.com/photo-1559526324-593bc073d938?w=300`
  - Gallery 3: `https://images.unsplash.com/photo-1534423861386-85a16f5d13fd?w=300`
  - Gallery 4: `https://images.unsplash.com/photo-1560419015-7c427e8ae5ba?w=300`

**CSS Eksternal:**
- Membuat file `style.css` terpisah untuk styling (tanpa inline styles)
- Menggunakan Google Fonts (Montserrat) untuk typography
- Implementasi design system yang konsisten dengan:
  - CSS classes terorganisir (`.hero-logo`, `.about-image`, `.gallery-grid`, `.gallery-image`, `.game-card`, dll)
  - Tidak ada duplikasi kode CSS
  - Semua styling terpusat di file CSS eksternal

---

## 2. Buat Kembali Halaman Landing Page agar Lebih Berwarna dengan Menggunakan Beberapa Gambar Berbeda

### Yang Telah Dilakukan:

**Palet Warna Biru Roblox:**
- **Primary Blue (#0066cc)**: Background section Beranda
- **Secondary Blue (#0052a3)**: Background section Tentang dan Galeri
- **Dark Blue (#003d7a)**: Background section Permainan
- **Darker Blue (#002855)**: Background navbar dan footer
- **Accent Blue (#00a8ff)**: Warna aksen untuk logo, hover effects, dan highlight

**Penggunaan Gambar Berbeda:**
- **Section Beranda**: Logo Roblox berbentuk lingkaran menggunakan class `.hero-logo` (350x350px desktop, 250x250px mobile)
- **Section Tentang**: Gambar ilustrasi tentang gaming menggunakan class `.about-image` (500px width desktop, 100% mobile)
- **Section Permainan**: 3 gambar berbeda untuk setiap game card dengan class `.game-image`:
  - Adopt Me: Gambar dari Viva Digital
  - Fishit: Gambar dari Roblox CDN
  - Brookhaven: Gambar dari Roblox CDN
- **Section Galeri**: 4 gambar berbeda menggunakan CSS Grid dengan class `.gallery-grid` dan `.gallery-image` dari Unsplash

**Efek Visual:**
- Border radius 10px pada semua gambar
- Hover effects pada game cards (transform translateY dan box-shadow)
- Box shadow pada navbar untuk depth
- Background semi-transparan pada game cards (rgba(255, 255, 255, 0.05))
- Transisi smooth pada semua hover effects (0.3s ease)

**Responsive Design:**
- **Games Grid**: Menggunakan CSS Grid `repeat(auto-fit, minmax(300px, 1fr))` yang menyesuaikan dari 3 kolom (desktop) ke 1 kolom (mobile ≤768px)
- **Gallery Grid**: Menggunakan CSS Grid `repeat(auto-fit, minmax(200px, 1fr))` yang menyesuaikan dari 4 kolom (desktop) ke 1 kolom (mobile ≤480px)
- Media queries untuk 2 breakpoint:
  - Tablet/Mobile: `@media (max-width: 768px)`
  - Small Mobile: `@media (max-width: 480px)`
- Semua gambar responsif dengan `object-fit: cover` untuk menjaga proporsi

---

## 3. Buat agar Menu di Atas Ketika Diklik Website Mengalir ke Bagian Website yang Diinginkan

### Yang Telah Dilakukan:

**Struktur Navigasi:**
- Membuat navbar fixed di bagian atas dengan 4 menu:
  - BERANDA → `#home`
  - TENTANG → `#about`
  - PERMAINAN → `#games`
  - GALERI → `#gallery`

**Smooth Scrolling:**
- Menambahkan `scroll-behavior: smooth;` pada CSS HTML element
- Setiap link menu menggunakan anchor link (`href="#section-id"`)
- Setiap section memiliki ID yang sesuai dengan link navigasi:
  - `<div id="home">` untuk section Beranda
  - `<div id="about">` untuk section Tentang
  - `<section id="games">` untuk section Permainan
  - `<div id="gallery">` untuk section Galeri

**Navbar Fixed:**
- Navbar menggunakan `position: fixed` agar selalu terlihat saat scroll
- Z-index 9999 untuk memastikan navbar di atas konten lain
- Padding-top pada section pertama (100px) untuk mengkompensasi tinggi navbar
- Navbar height: 60px dengan alignment yang konsisten

**Hover Effects:**
- Link menu berubah warna menjadi accent blue (#00a8ff) saat hover
- Background color berubah dengan transisi smooth (0.3s ease)
- Border radius 5px pada link untuk efek visual yang lebih baik

**Responsive Menu:**
- Toggle button untuk mobile dengan icon bar
- Collapse menu menggunakan Bootstrap collapse component
- Menu tetap berfungsi dengan smooth scrolling di semua device

---

## Teknologi yang Digunakan:

1. **HTML5**: Struktur semantik
2. **CSS3**: Styling dengan design system konsisten
3. **Bootstrap 3.4.1**: Framework untuk responsif dan komponen
4. **Google Fonts**: Montserrat untuk typography
5. **jQuery**: Untuk Bootstrap JavaScript components

## Fitur Tambahan:

- **Design System**: Konsisten dengan spacing, typography, dan warna
- **Responsive Layout**: Berfungsi optimal di desktop, tablet, dan mobile dengan CSS Grid
- **Accessibility**: Alt text pada semua gambar
- **Performance**: Menggunakan assets online yang dioptimalkan, kode CSS yang bersih tanpa duplikasi
- **User Experience**: Smooth scrolling dan hover effects yang halus
- **Code Quality**: 
  - Tidak ada inline styles (semua di CSS eksternal)
  - Struktur HTML yang bersih dan semantik
  - CSS Grid untuk layout modern dan fleksibel
  - Media queries yang terorganisir untuk responsive design

