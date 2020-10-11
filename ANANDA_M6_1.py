print(">>> Program Perhitungan Rata - Rata <<<")

#memasukkan kondisi try & except
try:
    #memasukkan inputan nilai Harian & UTS & UAS
    nilaiHarian = int(input("Masukkan Nilai Harian : "))
    nilaiUTS = int(input("Masukkan Nilai UTS : "))
    nilaiUAS = int(input("Masukkan Nilai UAS : "))
    #mencari rata rata dari ketiga nilai tersebut
    Total = (nilaiUTS + nilaiHarian + nilaiUAS)/3
    print("Nilai Rata - Rata = ",Total)
except ValueError:
    print("Inputan hanya menerima nilai dalam bentuk angka (Integer) ! ")

#except akan di pake jika kita melakukan kesalahan saat penginputan di kondisi try, except akan menangkap segala kemungkinan error tersebut
#jika kita memasukkan input yang benar maka hasil print try akan keluar, jika terjadi error maka print except yang akan keluar