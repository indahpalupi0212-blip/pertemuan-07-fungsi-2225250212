
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n===== UTILITAS MATEMATIKA =====")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def input_float(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            return nilai
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def input_integer_nonnegatif(pesan):
    while True:
        try:
            nilai = int(input(pesan))

            if nilai >= 0:
                return nilai
            else:
                print("Bilangan harus nonnegatif.")

        except ValueError:
            print("Input harus berupa bilangan bulat nonnegatif.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            p = input_float("Masukkan panjang: ")
            l = input_float("Masukkan lebar: ")

            if p < 0 or l < 0:
                print("Panjang dan lebar tidak boleh negatif.")
            else:
                hasil = luas_persegi_panjang(p, l)
                print(f"Luas persegi panjang = {hasil:g}")

        elif pilihan == "2":
            a = input_float("Masukkan alas: ")
            t = input_float("Masukkan tinggi: ")

            if a < 0 or t < 0:
                print("Alas dan tinggi tidak boleh negatif.")
            else:
                hasil = luas_segitiga(a, t)
                print(f"Luas segitiga = {hasil:g}")

        elif pilihan == "3":
            n = input_integer_nonnegatif("Masukkan n: ")
            hasil = jumlah_n(n)
            print(f"Jumlah 1 sampai {n} = {hasil}")

        elif pilihan == "4":
            n = input_integer_nonnegatif("Masukkan n: ")
            hasil = faktorial(n)
            print(f"Faktorial {n}! = {hasil}")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1 sampai 5.")


if __name__ == "__main__":
    main()
