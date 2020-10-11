#memasukkan inputan jumlah sayur
jumlah = int(input("Masukkan jumlah sayur: "))
#membuat list kosong 
listSayur = []
#menggunakan looping for karna list hanya dibatasi 4 saja
for i in range(4):
    sayur = input("Masukkan sayur ke-"+str(i+1)+":")
    #memasukkan inputan sayur kedalam list kosong yang telah dibuat menggunakan kode program append
    listSayur.append(sayur)

#membuat inputan urutan tengah notasi integer
urutan = int(input("Anda ingin menampilkan sayur urutan ke-berapa?"))-1
#menggunakan kondisi if elif else untuk mendeteksi apakah inputan urutan ada pada list sayur
if urutan in range(len(listSayur)):
    print("Sayur ke" + str(urutan),"adalah sayur"+str(listSayur[urutan]))
elif urutan not in range(len(listSayur)):
    print("Sayur tidak tersedia pada urutan tersebut")
    