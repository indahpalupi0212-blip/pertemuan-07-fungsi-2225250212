# Pertemuan 7 — Fungsi, Parameter, Return Value, dan Scope dalam Python

## Identitas Mahasiswa

- **Nama:** Indah Palupi Kusumaningrum
- **NIM:** 2225250212
- **Kelas:** 3F

## Deskripsi

Repository ini berisi hasil praktikum Algoritma dan Pemrograman Pertemuan 7 tentang fungsi, parameter, nilai balik (*return value*), dan ruang lingkup variabel (*scope*) dalam Python.

Praktikum dilakukan menggunakan Visual Studio Code (VS Code). Kegiatan meliputi pembuatan fungsi, penggunaan parameter, pengembalian nilai, perulangan, pengolahan data sederhana, serta demonstrasi variabel lokal dan global.

## Tujuan Praktikum

1. Memahami cara mendefinisikan dan memanggil fungsi dalam Python.
2. Memahami penggunaan parameter dan argumen.
3. Memahami penggunaan `return` untuk mengembalikan nilai dari fungsi.
4. Menerapkan fungsi untuk menyelesaikan permasalahan sederhana.
5. Memahami perbedaan variabel lokal dan variabel di luar fungsi.
6. Menguji program menggunakan beberapa test case.
7. Mengelola dan mengumpulkan hasil praktikum menggunakan GitHub.

## Struktur Folder

```text
pertemuan-07-fungsi-2225250212/
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
├── praktik/
│   └── utilitas_matematika.py
├── .gitignore
└── README.md
```

## Latihan

### 1. Fungsi Salam

File: `latihan/01_salam.py`

Latihan ini menggunakan fungsi `salam()` dengan dua parameter, yaitu nama dan kelas.

Fungsi menampilkan pesan sapaan serta informasi kelas untuk setiap orang yang dipanggil.

Contoh pemanggilan:

```python
salam("Alya", "2A")
salam("Bima", "2B")
```

Output yang diharapkan:

```text
Halo, Alya. Selamat belajar Python!
Kelas: 2A
Halo, Bima. Selamat belajar Python!
Kelas: 2B
```

**Konsep yang dipelajari:** fungsi, parameter, argumen, dan pemanggilan fungsi.

### 2. Fungsi Luas Persegi Panjang

File: `latihan/02_luas_persegi_panjang.py`

Program menghitung luas persegi panjang menggunakan fungsi `luas_persegi_panjang(p, l)`.

Rumus:

Luas = panjang × lebar

Fungsi menerima panjang dan lebar sebagai parameter, kemudian mengembalikan hasil perhitungan menggunakan `return`.

Test case:

| Panjang | Lebar | Hasil yang diharapkan |
|---:|---:|---:|
| 8 | 5 | 40 |
| 2.5 | 4 | 10.0 |
| 0 | 7 | 0 |

**Konsep yang dipelajari:** parameter, operasi aritmetika, dan nilai balik fungsi.

### 3. Fungsi Jumlah 1 sampai n

File: `latihan/03_jumlah_n.py`

Program menghitung jumlah seluruh bilangan bulat dari 1 sampai n menggunakan fungsi dan perulangan.

Rumus pembanding:

`jumlah = n × (n + 1) / 2`

Test case:

| Nilai n | Hasil yang diharapkan |
|---:|---:|
| 1 | 1 |
| 5 | 15 |
| 10 | 55 |
| 100 | 5050 |

Hasil perhitungan menggunakan perulangan dapat dibandingkan dengan hasil rumus untuk memastikan kebenaran program.

**Konsep yang dipelajari:** fungsi, perulangan, akumulasi, dan pengujian hasil.

### 4. Statistik Sederhana

File: `latihan/04_statistik_sederhana.py`

Program mengolah sekumpulan data untuk mendapatkan nilai minimum, maksimum, dan rata-rata.

Data pengujian:

```python
data = [70, 80, 65, 90, 75]
```

Hasil yang diharapkan:

- Nilai minimum: 65
- Nilai maksimum: 90
- Rata-rata: 76.0

Rata-rata diperoleh dengan membagi jumlah seluruh data dengan banyaknya data.

**Konsep yang dipelajari:** fungsi, list, pengolahan data, nilai minimum, nilai maksimum, dan rata-rata.

### 5. Demonstrasi Scope

File: `latihan/05_scope.py`

Latihan ini menunjukkan perbedaan variabel yang berada di luar fungsi dan variabel yang digunakan di dalam fungsi.

Contoh konsep:

```python
x = 10

def demo(x):
    y = x + 5
    print("di dalam fungsi:", x, y)
    return y

hasil = demo(20)

print("di luar fungsi:", x)
print("hasil:", hasil)
```

Output yang diharapkan:

```text
di dalam fungsi: 20 25
di luar fungsi: 10
hasil: 25
```

**Konsep yang dipelajari:** parameter fungsi, variabel lokal, variabel di luar fungsi, dan `return`.

## Praktik: Utilitas Matematika

File: `praktik/utilitas_matematika.py`

Program utilitas matematika menggabungkan beberapa fungsi ke dalam satu program berbasis menu.

Fungsi yang dibuat meliputi:

1. `luas_persegi_panjang(p, l)` untuk menghitung luas persegi panjang.
2. `luas_segitiga(a, t)` untuk menghitung luas segitiga.
3. `jumlah_n(n)` untuk menghitung jumlah bilangan dari 1 sampai n.
4. `faktorial(n)` untuk menghitung faktorial suatu bilangan.
5. `tampilkan_menu()` untuk menampilkan pilihan operasi.

Program menggunakan menu agar pengguna dapat memilih operasi matematika yang ingin dijalankan. Program juga melakukan validasi input, termasuk memastikan nilai n tidak negatif untuk operasi jumlah dan faktorial.

### Test Case Praktik

| Fungsi | Input | Hasil yang diharapkan |
|---|---|---:|
| Luas persegi panjang | p = 8, l = 5 | 40 |
| Luas segitiga | a = 10, t = 6 | 30.0 |
| Jumlah 1 sampai n | n = 10 | 55 |
| Faktorial | n = 5 | 120 |
| Faktorial | n = 0 | 1 |

## Cara Menjalankan Program

Pastikan Python telah terpasang dan dapat dijalankan melalui terminal VS Code.

### Menjalankan latihan

Buka terminal pada folder utama proyek, lalu jalankan salah satu perintah berikut:

```bash
python latihan/01_salam.py
```

Untuk latihan lainnya:

```bash
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
```

### Menjalankan program utilitas matematika

```bash
python praktik/utilitas_matematika.py
```

Jika perintah `python` tidak dikenali pada Windows, coba gunakan:

```bash
py latihan/01_salam.py
```

atau sesuaikan nama file dengan program yang ingin dijalankan.

## Pengujian Program

Pengujian dilakukan dengan menjalankan setiap file Python dan membandingkan hasil aktual dengan hasil yang diharapkan pada test case.

Kriteria pengujian:

- Fungsi menerima parameter sesuai kebutuhan.
- Fungsi mengembalikan atau menampilkan hasil yang benar.
- Perhitungan sesuai dengan rumus matematika.
- Variabel lokal dan variabel di luar fungsi menunjukkan perilaku sesuai scope.
- Program menangani input sesuai validasi yang diterapkan.

## Kesimpulan

Melalui praktikum Pertemuan 7, saya mempelajari penggunaan fungsi dalam Python, termasuk parameter, argumen, nilai balik dengan `return`, serta ruang lingkup variabel.

Saya juga menerapkan fungsi untuk menyelesaikan beberapa permasalahan, seperti menghitung luas bangun datar, menjumlahkan bilangan, menghitung statistik sederhana, dan menghitung faktorial.

Pengujian dengan beberapa test case membantu memastikan bahwa program menghasilkan keluaran sesuai dengan yang diharapkan.

## Pengumpulan melalui GitHub

Seluruh file praktikum disusun dalam satu repository dengan struktur folder yang telah ditentukan. File `README.md` digunakan untuk menjelaskan isi repository, tujuan praktikum, cara menjalankan program, dan hasil pengujian.

**Repository GitHub:** [Masukkan tautan repository GitHub kamu]
