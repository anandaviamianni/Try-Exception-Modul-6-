def cariPrima(bawah, atas):
    if(bawah < 2):
        bawah = 2
    count = (atas-bawah) + 1

    for angka in range(bawah, atas+1):
        for i in range(2, angka):
            if(angka %  i == 0):
                count -= 1
                break
    assert count >= 0, "Sesuatu yang tidak masuk akal terjadi, mhon ulangi program"
    return count

print("==== PROGRAM CARI PRIMA ====")
atas = int(input("Masukkan batas atas : "))
bawah = int(input("Masukkan batas bawah : "))
print("\nbanyak bil.prima : ", cariPrima(bawah,atas))