## **Nama : TRI WAHYU WIDYASTUTI**
## **NIM : 2411102441172**
## **Tgl-bln-thn : 1️⃣6️⃣-0️⃣4️⃣-2️⃣0️⃣2️⃣6️⃣**
___
# **➡️Tugas-Code-Audit-Minggu5**
## Repositori ini berisi hasil tugas praktikum Rekayasa Perangkat Lunak mengenai **Code Audit** dan penerapan prinsip **Clean Code**.
---
# **Deskripsi Proyek**
### Proyek ini adalah aplikasi kalkulator harga sederhana berbasis Python yang menghitung total pembayaran berdasarkan harga, diskon, dan status keanggotaan (member). Proyek dimulai dengan kode yang berantakan (*Legacy Code*) dan kemudian diperbaiki melalui proses *refactoring*.
---
# **Prinsip Clean Code yang Diterapkan**
Dalam proses audit, saya melakukan perbaikan berdasarkan prinsip-prinsip berikut:
* **Meaningful Naming**: Mengubah nama variabel dari satu huruf (`a, b, c`) menjadi nama yang deskriptif (`price, discount, is_member`).
* **Single Responsibility Principle (SRP)**: Memisahkan logika perhitungan matematika ke dalam fungsi tersendiri agar kode lebih terorganisir.
* **Don't Repeat Yourself (DRY)**: Menghilangkan duplikasi logika dengan menggunakan struktur data *list* dan perulangan (*loop*).
* **Magic Numbers**: Mengganti angka diskon statis `5000` menjadi variabel konstanta `ADDITIONAL_MEMBER_DISCOUNT`.
* **Formatting & Comments**: Merapikan indentasi dan menghapus komentar-komentar yang tidak perlu agar kode lebih bersih.
---
# **Cara Menjalankan Aplikasi**
1. Pastikan Python sudah terinstal di perangkat Anda.
2. Jalankan perintah berikut di terminal:
   ```bash
   python kalkulator.py
___