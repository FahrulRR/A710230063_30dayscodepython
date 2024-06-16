def tampilkan_menu():
    print("\n--- Aplikasi Pengelola Buku ---")
    print("1. Tambah buku")
    print("2. Lihat semua buku")
    print("3. Cari buku")
    print("4. Hapus buku")
    print("5. Keluar")

def baca_buku(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def tulis_buku(file_path, buku):
    with open(file_path, 'w') as file:
        for b in buku:
            file.write(b + '\n')

def tambah_buku(buku):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    buku_baru = f"{judul} oleh {penulis}"
    buku.append(buku_baru)
    print("Buku berhasil ditambahkan.")

def lihat_buku(buku):
    if not buku:
        print("Tidak ada buku untuk ditampilkan.")
    else:
        for idx, b in enumerate(buku, start=1):
            print(f"{idx}. {b}")

def cari_buku(buku):
    kriteria = input("Masukkan kata kunci untuk mencari buku: ").lower()
    hasil = [b for b in buku if kriteria in b.lower()]
    if not hasil:
        print("Buku tidak ditemukan.")
    else:
        for b in hasil:
            print(b)

def hapus_buku(buku):
    lihat_buku(buku)
    nomor = int(input("Masukkan nomor buku yang akan dihapus: ")) - 1
    if 0 <= nomor < len(buku):
        buku.pop(nomor)
        print("Buku berhasil dihapus.")
    else:
        print("Nomor buku tidak valid.")

def main():
    file_path = "buku.txt"
    buku = baca_buku(file_path)
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            tambah_buku(buku)
            tulis_buku(file_path, buku)
        elif pilihan == '2':
            lihat_buku(buku)
        elif pilihan == '3':
            cari_buku(buku)
        elif pilihan == '4':
            hapus_buku(buku)
            tulis_buku(file_path, buku)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan Aplikasi Pengelola Buku. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
