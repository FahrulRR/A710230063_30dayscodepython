# Struktur dasar aplikasi
import os

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n--- Aplikasi Pengelola Kontak ---")
    print("1. Tambah kontak")
    print("2. Lihat semua kontak")
    print("3. Cari kontak")
    print("4. Hapus kontak")
    print("5. Keluar")

# Fungsi untuk membaca kontak dari file
def baca_kontak(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        kontak = [line.strip().split(',') for line in file.readlines()]
    return kontak

# Fungsi untuk menulis kontak ke file
def tulis_kontak(file_path, kontak):
    with open(file_path, 'w') as file:
        for k in kontak:
            file.write(','.join(k) + '\n')

# Fungsi untuk menambah kontak baru
def tambah_kontak(kontak):
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    kontak.append([nama, nomor, email])
    print("Kontak berhasil ditambahkan.")

# Fungsi untuk menampilkan semua kontak
def lihat_kontak(kontak):
    if not kontak:
        print("Tidak ada kontak untuk ditampilkan.")
    else:
        for idx, k in enumerate(kontak, start=1):
            print(f"{idx}. Nama: {k[0]}, Nomor: {k[1]}, Email: {k[2]}")

# Fungsi untuk mencari kontak
def cari_kontak(kontak):
    kriteria = input("Masukkan nama atau nomor telepon untuk mencari: ")
    hasil = [k for k in kontak if kriteria in k]
    if not hasil:
        print("Kontak tidak ditemukan.")
    else:
        for k in hasil:
            print(f"Nama: {k[0]}, Nomor: {k[1]}, Email: {k[2]}")

# Fungsi untuk menghapus kontak
def hapus_kontak(kontak):
    lihat_kontak(kontak)
    nomor = int(input("Masukkan nomor kontak yang akan dihapus: ")) - 1
    if 0 <= nomor < len(kontak):
        kontak.pop(nomor)
        print("Kontak berhasil dihapus.")
    else:
        print("Nomor kontak tidak valid.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    file_path = "kontak.txt"
    kontak = baca_kontak(file_path)
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            tambah_kontak(kontak)
            tulis_kontak(file_path, kontak)
        elif pilihan == '2':
            lihat_kontak(kontak)
        elif pilihan == '3':
            cari_kontak(kontak)
        elif pilihan == '4':
            hapus_kontak(kontak)
            tulis_kontak(file_path, kontak)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan Aplikasi Pengelola Kontak. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
