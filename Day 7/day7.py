 # Menentukan bilangan prima atau tidak
def apakah_prima(angka):
    if angka > 1:
        for i in range(2, int(angka**0.5) + 1):
            if (angka % i) == 0:
                print("Bukan bilangan prima")
                break
        else:
            print("bilangan prima")
    else:
        print("Bukan bilangan prima")

# Proses
angka_input = int(input("Masukan sebuah bilangan: "))
apakah_prima(angka_input)