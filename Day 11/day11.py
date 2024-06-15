# Struktur dasar aplikasi
import os

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n--- Kalkulator Sederhana ---")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Riwayat")
    print("6. Keluar")

# Fungsi untuk membaca riwayat dari file
def baca_riwayat(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        riwayat = [line.strip() for line in file.readlines()]
    return riwayat

# Fungsi untuk menulis riwayat ke file
def tulis_riwayat(file_path, riwayat):
    with open(file_path, 'w') as file:
        for item in riwayat:
            file.write(item + '\n')

# Fungsi untuk melakukan penjumlahan
def penjumlahan(a, b):
    return a + b

# Fungsi untuk melakukan pengurangan
def pengurangan(a, b):
    return a - b

# Fungsi untuk melakukan perkalian
def perkalian(a, b):
    return a * b

# Fungsi untuk melakukan pembagian
def pembagian(a, b):
    if b == 0:
        return "Kesalahan: Pembagian dengan nol"
    return a / b

# Fungsi untuk menampilkan riwayat
def tampilkan_riwayat(riwayat):
    if not riwayat:
        print("Tidak ada riwayat untuk ditampilkan.")
    else:
        for item in riwayat:
            print(item)

# Fungsi utama untuk menjalankan aplikasi
def main():
    file_path = "riwayat.txt"
    riwayat = baca_riwayat(file_path)
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi: ")
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
                continue

            if pilihan == '1':
                hasil = penjumlahan(a, b)
                operasi = "Penjumlahan"
            elif pilihan == '2':
                hasil = pengurangan(a, b)
                operasi = "Pengurangan"
            elif pilihan == '3':
                hasil = perkalian(a, b)
                operasi = "Perkalian"
            elif pilihan == '4':
                hasil = pembagian(a, b)
                operasi = "Pembagian"
            
            print(f"Hasil {operasi} {a} dan {b} adalah {hasil}")
            riwayat.append(f"{operasi} {a} dan {b} = {hasil}")
            tulis_riwayat(file_path, riwayat)
        
        elif pilihan == '5':
            tampilkan_riwayat(riwayat)
        
        elif pilihan == '6':
            print("Terima kasih telah menggunakan Kalkulator Sederhana. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
