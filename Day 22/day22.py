def kuadrat_bilangan():
    while True:
        try:
            # Meminta input dari user
            bilangan = int(input("Masukkan bilangan bulat: "))
            # Menghitung hasil kuadrat
            hasil = bilangan ** 2
            # Mencetak hasil
            print(f"Hasil kuadrat dari {bilangan} adalah {hasil}")
            break
        except ValueError:
            # Menampilkan pesan error jika input tidak valid
            print("Input yang dimasukkan tidak valid! Silakan masukkan bilangan bulat yang valid.")

# Memanggil fungsi
kuadrat_bilangan()
