# 🎧 PodMatch — Analisis Mood & Rekomendasi Podcast  

![PodMatch](https://img.shields.io/badge/PodMatch-Machine%20Learning-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

PodMatch adalah aplikasi web berbasis Flask yang dapat **menganalisis mood pengguna berdasarkan teks** dan memberikan **rekomendasi podcast** yang sesuai dengan mood tersebut. Riwayat pencarian juga disimpan secara lokal, sehingga pengguna dapat melihat kembali hasil mood & rekomendasi podcast sebelumnya.

PodMatch dibuat untuk membantu pengguna menemukan konten audio yang sesuai dengan emosi mereka supaya dapat membantu memperbaiki mood mereka secara cepat dan akurat.

---

## 🚀 Fitur Utama

### 🧠 Analisis Mood
- Menggunakan model NLP untuk membaca teks yang dimasukkan pengguna.
- Menentukan mood seperti: **Senang, Sedih, Marah, Takut, Kasih, atau Netral**.

### 🎙 Rekomendasi Podcast
- Setiap mood akan menghasilkan rekomendasi podcast YouTube yang sesuai.
- Podcast ditampilkan dengan **thumbnail**, **judul**, dan **tombol play**.

### 📜 Riwayat Mood
- Semua analisis sebelumnya disimpan secara otomatis di **localStorage**.
- Ditampilkan dalam bentuk kartu (card) berisi:
  - Mood
  - Tanggal analisis
  - Judul podcast
  - Thumbnail video
  - Teks yang dimasukkan pengguna

### 🗑 Hapus Riwayat
- Tombol **Hapus Riwayat** hanya muncul jika data tersedia.
- Dilengkapi **popup konfirmasi** sebelum penghapusan.

### 🎨 Tampilan Modern & Responsif
- Desain UI berwarna gelap (dark theme).
- Mobile-friendly, clean, dan elegan.

---

## 🛠 Teknologi yang Digunakan

- **HTML + Jinja2 (Flask template)**
- **CSS Custom + Bootstrap**
- **JavaScript (Frontend Logic)**
- **Flask / Python Backend**
- **LocalStorage** untuk menyimpan riwayat mood
- **Youtube API v3**
- **YouTube Podcast Embedding** melalui link dan thumbnail

---

## 📥 Instalasi & Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/username/podmatch.git
```
```bash
cd podmatch
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi
```bash
flask run
```
atau
```bash
python app.py
```

### 4. Akses di browser
```bash
http://127.0.0.1:5000/
```
