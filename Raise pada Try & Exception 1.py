try:
    x = "Hello World"
    if not type(x) is int:
        raise TypeError("Hanya tipe data integer yang diperbolehkan")
except:
    print("Terjadi Error")
finally:
    print("Program telah selesai")