namaAnak = ["Ziaf", "Ziza", "Eded"]
print("== Aplikasi Pencatat Absensi ===")
try:
    jumlahsiswa = int(input("Masukkan Jumlah Siswa yang ingin ditambahkan : "))
    for i in range(jumlahsiswa):
        namasiswa = str(input("Masukkan Nama Siswa : "))
        namaAnak.append(namasiswa)
    urutan = int(input("Anda ingin menampilkan siswa absen pada urutan ke - "))-1
    print(namaAnak[urutan])
except IndexError:
    print("Siswa tersebut tidak ada dalam absen")
else:
    print("Siswa tersebut alfa")
finally:
    print("Program Selesai")
