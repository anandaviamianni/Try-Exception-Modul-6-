try: 
    nilaiUTS = int(input("Masukkan Nilai UTS Anda ! : "))
except ValueError:
    print("Program ini hanya menerima jenis nilai integer ! ")
else:
    print("StayAtHomeAjah!")


# Jika angka yang dimasukkan akan mengeluarkan output else
# jika tidak sesuai akan mengeluarkan output except