try:
    angka = int(input())
    angka2 = int(input())
    angka3 = angka/angka2
    print(angka3)
except ValueError:
    print("Maaf, Inputan hanya menerima angka")
except ZeroDivisionError:
    print("Program Error")