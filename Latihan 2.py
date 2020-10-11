# Kamu adalah seorang praktikan Algoritma dan Pemrograman yang ingin mencoba hal baru. 
# Kenallah kamu dengan Sushi seorang saudagar cemerlang yang ingin mendapatkan keuntungan dari 
# memonopoli stok di 4 pasar. Sebut saja Pasar 0, Pasar 1, Pasar 2, dan Pasar 3. Sushi ingin kamu membuatkan 
# program sederhana yang mengecek jumlah stok suatu buah yang kurang dari 20 berada di Pasar apa.  
# Buatlah program tersebut demi bayaran yang mahal dengan usaha seminimal mungkin!

stokBuah = {
    "pisang" : [120, 40, "sejumlah banyak banget pokoknya", 21],
    'apel' : [40, 32, 22, 28],
    'mangga' : [80, 12, 10, 23],
    'naga' : [16, 14, 16, 16]
}
try:
    cariBuah = str(input("Masukkan nama buah yang ingin dicari: "))
    cariPasar = int(input("Masukkan nomor pasar yang ingin dicari: "))
    print()
    if(stokBuah[cariBuah][cariPasar] < 20):
        print("Kesimpulan:\n")
        print("Stok buah masih banyak. Pasar dan buah ini tidak cocok untuk dimonopoli.")
except KeyError:
    print(f"Buah dengan nama {cariBuah} bukan merupakan target Sushi")
except IndexError:
    print(f"Pasar ke-{cariPasar} bukan merupakan target Sushi")
except TypeError:
    print("Stok buah tidak bisa dihitung")
    print("Stok buah " + str(cariBuah) + " di Pasar ke-"+ str(cariPasar)+ " adalah " + str(stokBuah[cariBuah][cariPasar]))
finally:
    print("\n== ini batas bantuan yang program ini dapat lakukan =="+
            "\n\t-Apa tindakanmu selanjutnya?-")