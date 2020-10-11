class PenangananErrorKhusus(Exception):
    def __init__(self):
        pass
    def tampil(self):
        return ("Program hanya bisa dijalankan jika batas bawah " + 
                "yang dimasukan lebih dari 1")

def cariPrima(bawah, atas):
    try:
        if(bawah < 2):
            raise PenangananErrorKhusus()
        count = (atas-bawah) + 1
        
        for angka in range(bawah, atas +1):
            for i in range(2,angka):
                if (angka%i == 0):
                    count -= 1
                    break

    except PenangananErrorKhusus as x :
        print(x.tampil())
        bawahBaru = int(input("Masukkan batas bawah : "))
        return cariPrima(bawahBaru, atas)
    else:
        return count

print("==== PROGRAM CARI PRIMA ====")
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
print("\nbanyak bil. prima:", cariPrima(bawah, atas))
print()