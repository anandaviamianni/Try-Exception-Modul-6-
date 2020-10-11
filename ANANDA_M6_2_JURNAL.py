print("=== Operasi Pembagian ===")

try:
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    total = angka1 / angka2
    print("Hasil Pembagian : ",int(total))
except ZeroDivisionError:
    print("Program mengandung pembagian 0 !")
except ValueError:
    print("Program ini hanya menerima inputan ")
else:
    print("Program Berjalan dengan baik ! ")
finally:
    print("Program Selesai !")