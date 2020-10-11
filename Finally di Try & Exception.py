try:
    nilaiUTS = int(input("Masukkan Nilai UTS Anda ! : "))
except ValueError:
    print("Program ini hanya menerima jenis nilai integer! ")
else:
    print("#StayAtHomeAjah")
finally:
    print("Program telah selesai")

#Kode finally akan selalu berjalan tanpa mempedulikan error atau tidak