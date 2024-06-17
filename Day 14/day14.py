# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n--- Aplikasi Pengelola Inventaris Barang ---")
    print("1. Tambah barang")
    print("2. Lihat semua barang")
    print("3. Cari barang")
    print("4. Hapus barang")
    print("5. Keluar")

# Fungsi untuk menambah barang baru
def tambah_barang(inventaris):
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))
    barang_baru = {"nama": nama, "jumlah": jumlah, "harga": harga}
    inventaris.append(barang_baru)
    print("Barang berhasil ditambahkan.")

# Fungsi untuk menampilkan semua barang
def lihat_barang(inventaris):
    if not inventaris:
        print("Tidak ada barang dalam inventaris.")
    else:
        print("\nDaftar Barang:")
        for idx, barang in enumerate(inventaris, start=1):
            print(f"{idx}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

# Fungsi untuk mencari barang
def cari_barang(inventaris):
    kata_kunci = input("Masukkan nama barang yang dicari: ").lower()
    hasil = [barang for barang in inventaris if kata_kunci in barang['nama'].lower()]
    if not hasil:
        print("Barang tidak ditemukan.")
    else:
        print("\nHasil Pencarian:")
        for barang in hasil:
            print(f"Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

# Fungsi untuk menghapus barang
def hapus_barang(inventaris):
    lihat_barang(inventaris)
    nomor = int(input("Masukkan nomor barang yang akan dihapus: ")) - 1
    if 0 <= nomor < len(inventaris):
        inventaris.pop(nomor)
        print("Barang berhasil dihapus.")
    else:
        print("Nomor barang tidak valid.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    inventaris = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tambah_barang(inventaris)
        elif pilihan == '2':
            lihat_barang(inventaris)
        elif pilihan == '3':
            cari_barang(inventaris)
        elif pilihan == '4':
            hapus_barang(inventaris)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan Aplikasi Pengelola Inventaris Barang. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
