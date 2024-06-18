# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa(daftar_mahasiswa, nama, nim, jurusan):
    mahasiswa_baru = Mahasiswa(nama, nim, jurusan)
    daftar_mahasiswa.append(mahasiswa_baru)
    return daftar_mahasiswa

# Fungsi untuk melihat semua mahasiswa
def lihat_mahasiswa(daftar_mahasiswa):
    if not daftar_mahasiswa:
        return "Tidak ada data mahasiswa."
    else:
        result = []
        for idx, mhs in enumerate(daftar_mahasiswa, start=1):
            result.append(f"{idx}. Nama: {mhs.nama}, NIM: {mhs.nim}, Jurusan: {mhs.jurusan}")
        return "\n".join(result)

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(daftar_mahasiswa, nim):
    hasil = [mhs for mhs in daftar_mahasiswa if mhs.nim == nim]
    if not hasil:
        return "Mahasiswa tidak ditemukan."
    else:
        result = []
        for mhs in hasil:
            result.append(f"Nama: {mhs.nama}, NIM: {mhs.nim}, Jurusan: {mhs.jurusan}")
        return "\n".join(result)

# Fungsi untuk menghapus mahasiswa berdasarkan nomor urut
def hapus_mahasiswa(daftar_mahasiswa, nomor):
    if 0 <= nomor < len(daftar_mahasiswa):
        daftar_mahasiswa.pop(nomor)
        return "Mahasiswa berhasil dihapus."
    else:
        return "Nomor mahasiswa tidak valid."

# Fungsi untuk melihat jurusan unik
def lihat_jurusan_unik(daftar_mahasiswa):
    jurusan_set = {mhs.jurusan for mhs in daftar_mahasiswa}
    if not jurusan_set:
        return "Tidak ada jurusan dalam data mahasiswa."
    else:
        result = ["Jurusan unik:"]
        for jurusan in jurusan_set:
            result.append(jurusan)
        return "\n".join(result)

# Contoh penggunaan fungsi-fungsi
if __name__ == "__main__":
    daftar_mahasiswa = []

    # Tambah beberapa mahasiswa
    daftar_mahasiswa = tambah_mahasiswa(daftar_mahasiswa, "Budi", "123", "Informatika")
    daftar_mahasiswa = tambah_mahasiswa(daftar_mahasiswa, "Siti", "124", "Teknik Mesin")
    
    # Lihat semua mahasiswa
    print(lihat_mahasiswa(daftar_mahasiswa))
    
    # Cari mahasiswa berdasarkan NIM
    print(cari_mahasiswa(daftar_mahasiswa, "123"))
    
    # Hapus mahasiswa berdasarkan nomor urut dalam daftar
    print(hapus_mahasiswa(daftar_mahasiswa, 0))
    
    # Lihat semua mahasiswa setelah dihapus
    print(lihat_mahasiswa(daftar_mahasiswa))
    
    # Lihat jurusan unik
    print(lihat_jurusan_unik(daftar_mahasiswa))
