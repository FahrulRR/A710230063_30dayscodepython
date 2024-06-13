# Membuat kartu mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"Data mahasiswa:\nNim: {self.nim}\nNama: {self.nama}\nAngkatan: {self.angkatan}\nProdi: {self.prodi}")


mahasiswa = Mahasiswa("A710230063", "Fahrul Rachmad R", 2023, "PTI")

mahasiswa.kartu_mahasiswa()
