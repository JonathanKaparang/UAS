import json

# data perpustakaan
perpustakaan = []

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    tahun_terbit = int(input("Masukkan tahun terbit: "))
    kategori = input("Masukkan kategori buku: ")
    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun_terbit,
        "kategori": kategori,
        "dipinjam": False
    }
    perpustakaan.append(buku_baru)
    print("Buku berhasil ditambahkan!")

def hapus_buku():
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    for i, buku in enumerate(perpustakaan):
        if buku["judul"] == judul:
            del perpustakaan[i]
            print("Buku berhasil dihapus!")
            return
    print("Buku tidak ditemukan!")

def cari_buku(keyword, field):
    hasil_pencarian = []
    for buku in perpustakaan:
        if buku[field] == keyword:
            hasil_pencarian.append(buku)
    if hasil_pencarian:
        for buku in hasil_pencarian:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun Terbit: {buku['tahun_terbit']}, Kategori: {buku['kategori']}")
    else:
        print("Buku tidak ditemukan!")

def pinjam_buku():
    judul = input("Masukkan judul buku yang ingin dipinjam: ")
    for buku in perpustakaan:
        if buku["judul"] == judul and not buku["dipinjam"]:
            buku["dipinjam"] = True
            print("Buku berhasil dipinjam!")
            return
    print("Buku tidak tersedia atau sudah dipinjam!")

def kembalikan_buku():
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
    for buku in perpustakaan:
        if buku["judul"] == judul and buku["dipinjam"]:
            buku["dipinjam"] = False
            print("Buku berhasil dikembalikan!")
            return
    print("Buku tidak ditemukan atau belum pernah dipinjam!")

def tampilkan_buku_dipinjam():
    buku_dipinjam = [buku for buku in perpustakaan if buku["dipinjam"]]
    if buku_dipinjam:
        for buku in buku_dipinjam:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}")
    else:
        print("Tidak ada buku yang sedang dipinjam.")

def simpan_data():
    with open("perpustakaan.json", "w") as file:
        json.dump(perpustakaan, file)
    print("Data perpustakaan berhasil disimpan!")

def muat_data():
    global perpustakaan
    try:
        with open("perpustakaan.json", "r") as file:
            perpustakaan = json.load(file)
        print("Data perpustakaan berhasil dimuat!")
    except FileNotFoundError:
        print("File data perpustakaan belum ada.")

# Muat data dari file JSON
muat_data()

# Menu utama
while True:
    print("\nMenu Perpustakaan:")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Cari Buku")
    print("4. Pinjam Buku")
    print("5. Kembalikan Buku")
    print("6. Tampilkan Buku yang Dipinjam")
    print("7. Simpan Data")
    print("8. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        hapus_buku()
    elif pilihan == "3":
        keyword = input("Masukkan kata kunci pencarian: ")
        field = input("Cari berdasarkan (judul/penulis/kategori): ")
        cari_buku if [field] == keyword else print("pencarian tidak ditemukan!")
    elif pilihan == "4":
        pinjam_buku()
    elif pilihan == "5":
        kembalikan_buku()
    elif pilihan == "6":
        tampilkan_buku_dipinjam()
    elif pilihan == "7":
        simpan_data()
    elif pilihan == "8":
        break
    else:
        print("Pilihan tidak valid!")