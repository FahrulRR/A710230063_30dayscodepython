# Buku Telepon Sederhana
daftar_kontak = ["Alice", "Bob", "Charlie", "David"]
nomor_telepon = ("123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123")
kontak_favorit = {"Alice", "Charlie"}
detail_kontak = {"Alice": {"alamat": "Jalan A No. 1", "email": "alice@example.com"}, "Bob": {"alamat": "Jalan B No. 2", "email": "bob@example.com"},"Charlie": {"alamat": "Jalan C No. 3", "email": "charlie@example.com"},"David": {"alamat": "Jalan D No. 4", "email": "david@example.com"}}

def tampilkan_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak):
    for i, nama in enumerate(daftar_kontak):
        favorit = "Ya" if nama in kontak_favorit else "Tidak"
        print(f"{nama}: {nomor_telepon[i]}, Favorit: {favorit}, {detail_kontak[nama]}")

def tambah_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak, nama, nomor, alamat, email, favorit=False):
    daftar_kontak.append(nama)
    nomor_telepon += (nomor,)
    if favorit: kontak_favorit.add(nama)
    detail_kontak[nama] = {"alamat": alamat, "email": email}
    return daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak

def hapus_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak, nama):
    if nama in daftar_kontak:
        i = daftar_kontak.index(nama)
        daftar_kontak.remove(nama)
        nomor_telepon = nomor_telepon[:i] + nomor_telepon[i+1:]
        kontak_favorit.discard(nama)
        del detail_kontak[nama]
    return daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak

# Contoh penggunaan 
tampilkan_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak)
print()
daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak = tambah_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak, "Eve", "567-890-1234", "Jalan E No. 5", "eve@example.com", favorit=True)
tampilkan_kontak(daftar_kontak, nomor_telepon, kontak_favorit, detail_kontak)
