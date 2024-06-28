class Tiket:
    def __init__(self, harga):
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah

class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__(harga=50000)  # Harga tiket biasa Rp 50,000

class TiketVIP(Tiket):
    def __init__(self):
        super().__init__(harga=100000)  # Harga tiket VIP Rp 100,000

class TiketGold(Tiket):
    def __init__(self):
        super().__init__(harga=150000)  # Harga tiket Gold Rp 150,000

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold) : ").strip().lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket : "))

    if jenis_tiket == 'biasa':
        tiket = TiketBiasa()
    elif jenis_tiket == 'vip':
        tiket = TiketVIP()
    elif jenis_tiket == 'gold':
        tiket = TiketGold()
    else:
        print("Jenis tiket tidak valid!")
        return

    total_harga = tiket.hitung_total(jumlah_tiket)
    print(f"Total Harga Tiket : Rp {total_harga}")

if __name__ == "__main__":
    main()
