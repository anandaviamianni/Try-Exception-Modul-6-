while True:
  try:
    angka = int(input())
    for i in range(3,angka,2):
      print(i, end = "  ")
    break
  except ValueError:
    print("Maaf, Inputan hanya menerima angka")
  break