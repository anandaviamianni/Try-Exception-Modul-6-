try:
    print("Program Pencarian Rata Rata Nilai")
    nilaiUTS = "80"
    nilaiUAS = int(input("Masukkan Nilai UAS Anda : "))
    Total = nilaiUTS + nilaiUAS
except TypeError:
    print("Tipe data yang digunakan tidak sesuai")
except ValueError:
    print("Program ini hanya menerima jenis nilai integer !")
except NameError:
    print("Salah penulisan variabel")