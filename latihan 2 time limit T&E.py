try:
    def tambah (angka_satu, angka_dua):
        try:
            return int(angka_satu)+int(angka_dua)
        except:
            print("Maaf input hanya bisa angka")
except ValueError:
    print("Maaf input hanya bisa angka")