#Inputan Belanja
jumlah_barang = int(input('Masukkan jumlah barang : '))
harga_barang = int(input('Masukkan harga barang : '))
total_harga = jumlah_barang * harga_barang

file = open('invoice.txt', 'w')
file.write('------------RINCIAN------------\n')
file.write(f'Jumlah Buku   : {jumlah_barang}\n')
file.write(f'Harga Buku    : Rp. {harga_barang}\n')
file.write('\n')
file.write(f'TOTAL         : Rp. {total_harga}\n')
file.close()

print()
print('------------RINCIAN------------')
print(f'Jumlah Buku   : {jumlah_barang}')
print(f'Harga Buku    : Rp. {harga_barang}')
print()
print(f'TOTAL         : Rp. {total_harga}')