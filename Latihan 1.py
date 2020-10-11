# Anda diminta untuk membuat program operasi pembagian dengan handling exception untuk menangani error apabila membagi bilangan dengan angka 0

try:
    print("====Operasi Pembagian====")
    k = int(input("Masukkan angka pertama: "))
    l = int(input("Masukkan angka kedua: "))
    m = k/l
    print("hasil pembagian : ",m)
except ZeroDivisionError:
    print("Anda tidak dapat membagi bilangan dengan angka 0")
