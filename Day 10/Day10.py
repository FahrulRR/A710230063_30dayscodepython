# Kelas Induk
class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies
    
    def buat_suara(self):
        return "Suara umum"
    
    def info(self):
        return f"{self.nama} adalah seekor {self.spesies}"

# Kelas Turunan
class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")  # Memanggil konstruktor dari kelas induk
        self.ras = ras
    
    def buat_suara(self):
        return "Guk guk"
    
    def info(self):
        info_induk = super().info()
        return f"{info_induk} dan berjenis {self.ras}"

# Menggunakan kelas
hewan_umum = Hewan("Hewan Umum", "Spesies Tidak Diketahui")
print(hewan_umum.info())
print(hewan_umum.buat_suara())

print()

anjing_saya = Anjing("Buddy", "Golden Retriever")
print(anjing_saya.info())
print(anjing_saya.buat_suara())
