print("Program Penentu Index")
try:
    nem= int(input("Masukkan NEM Anda! : "))
    if nem >= 80:
        print ("Index Kamu adalah : A")
    elif nem < 80 and nem >= 40:
        print ("Index Kamu adalah : B")
    else:
        print ("Index Kamu adalah : C")
except ValueError :
    print("Nilai NEM hanya berbentuk angka")
finally :
    print("Program Selesai")