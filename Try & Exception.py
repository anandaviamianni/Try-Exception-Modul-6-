try:
    nilaiUTS = int(input("Masukkan Niai UTS Anda ! : "))
except ValueError: 
    print("Program ini hanya enerima jenis nilai Integer !")

# # ValueError terjadi ketika operasi atau
# fungsi bawaan menerima argumen
# yang memiliki tipe yang tepat tetapi nilai
# yang tidak sesuai,