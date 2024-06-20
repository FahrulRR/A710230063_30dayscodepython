# Fungsi untuk menambahkan buku ke perpustakaan
def tambah_buku(nama_file, judul, penulis):
    with open(nama_file, 'a') as file:
        file.write(f"{judul},{penulis}\n")
    print(f"Buku '{judul}' oleh {penulis} telah ditambahkan.")

# Fungsi untuk menampilkan semua buku di perpustakaan
def lihat_buku(nama_file):
    try:
        with open(nama_file, 'r') as file:
            buku_list = file.readlines()
        
        if not buku_list:
            print("Belum ada buku yang ditambahkan.")
        else:
            print("Daftar Buku:")
            for buku in buku_list:
                judul, penulis = buku.strip().split(',')
                print(f"Judul: {judul}, Penulis: {penulis}")
    except FileNotFoundError:
        print("Belum ada buku yang ditambahkan.")

# Fungsi untuk mencari buku berdasarkan judul
def cari_buku(nama_file, judul):
    try:
        with open(nama_file, 'r') as file:
            buku_list = file.readlines()
        
        found = False
        for buku in buku_list:
            buku_judul, penulis = buku.strip().split(',')
            if buku_judul.lower() == judul.lower():
                print(f"Judul: {buku_judul}, Penulis: {penulis}")
                found = True
                break
        
        if not found:
            print(f"Buku dengan judul '{judul}' tidak ditemukan.")
    except FileNotFoundError:
        print("Belum ada buku yang ditambahkan.")

# Fungsi utama untuk mengoperasikan program
def main():
    nama_file = 'library.txt'
    
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Cari Buku")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            tambah_buku(nama_file, judul, penulis)
        elif pilihan == '2':
            lihat_buku(nama_file)
        elif pilihan == '3':
            judul = input("Masukkan judul buku yang dicari: ")
            cari_buku(nama_file, judul)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
