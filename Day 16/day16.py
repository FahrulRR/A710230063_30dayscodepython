# Fungsi untuk menambah buku baru ke dalam koleksi perpustakaan
def tambah_buku(perpustakaan, judul, penulis, tahun):
    buku = {
        'judul': judul,
        'penulis': penulis,
        'tahun': tahun
    }
    perpustakaan.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan ke dalam koleksi perpustakaan.")

# Fungsi untuk menampilkan semua buku yang ada dalam koleksi perpustakaan
def tampilkan_buku(perpustakaan):
    if not perpustakaan:
        print("Tidak ada buku dalam koleksi perpustakaan.")
    else:
        print("Daftar buku dalam koleksi perpustakaan:")
        for idx, buku in enumerate(perpustakaan, start=1):
            print(f"{idx}. {buku['judul']} oleh {buku['penulis']} ({buku['tahun']})")

# Fungsi untuk mencari buku berdasarkan judul
def cari_buku(perpustakaan, judul):
    hasil_cari = [buku for buku in perpustakaan if buku['judul'].lower() == judul.lower()]
    if not hasil_cari:
        print(f"Buku dengan judul '{judul}' tidak ditemukan dalam koleksi perpustakaan.")
    else:
        print(f"Buku dengan judul '{judul}' ditemukan:")
        for buku in hasil_cari:
            print(f"{buku['judul']} oleh {buku['penulis']} ({buku['tahun']})")

# Fungsi untuk menghapus buku berdasarkan judul
def hapus_buku(perpustakaan, judul):
    for buku in perpustakaan:
        if buku['judul'].lower() == judul.lower():
            perpustakaan.remove(buku)
            print(f"Buku '{judul}' berhasil dihapus dari koleksi perpustakaan.")
            return
    print(f"Buku dengan judul '{judul}' tidak ditemukan dalam koleksi perpustakaan.")

# Fungsi utama untuk menjalankan program pengelola buku perpustakaan
def main():
    perpustakaan = []
    while True:
        print("\nPengelola Buku Perpustakaan")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            tahun = input("Masukkan tahun terbit: ")
            tambah_buku(perpustakaan, judul, penulis, tahun)
        elif pilihan == '2':
            tampilkan_buku(perpustakaan)
        elif pilihan == '3':
            judul = input("Masukkan judul buku yang ingin dicari: ")
            cari_buku(perpustakaan, judul)
        elif pilihan == '4':
            judul = input("Masukkan judul buku yang ingin dihapus: ")
            hapus_buku(perpustakaan, judul)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan Pengelola Buku Perpustakaan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

if __name__ == "__main__":
    main()
