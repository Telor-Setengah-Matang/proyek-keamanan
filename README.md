# proyek-keamanan
# 🔒 Zero-Knowledge Password Manager (CLI-Based)

Aplikasi manajemen kata sandi berbasis *Command Line Interface* (CLI) yang mengimplementasikan arsitektur **Zero-Knowledge**. Aplikasi ini memastikan kredensial pengguna dienkripsi secara lokal di sisi klien sebelum disimpan, sehingga pihak ketiga maupun pengembang tidak dapat mengintip sandi asli.

Proyek ini dibangun untuk memenuhi kriteria Proyek Akhir mata kuliah **Digital Foundations / Rekayasa Perangkat Lunak (Topik: Keamanan & Privasi)**.

---

## 🚀 Fitur Utama
1. **Master Password Authentication**: Akses gerbang utama menggunakan satu kunci utama yang aman.
2. **Local End-to-End Encryption**: Kredensial dienkripsi langsung di perangkat sebelum masuk ke media penyimpanan.
3. **Decryption on Demand**: Data sandi hanya didekripsi ketika dipanggil oleh pengguna yang sah.

---

## 🛠️ Panduan Instalasi & Penggunaan

### 1. Prasyarat
Pastikan komputer Anda sudah terinstal **Python 3.x**. Anda dapat mengeceknya melalui terminal/command prompt:
```bash
python --version
