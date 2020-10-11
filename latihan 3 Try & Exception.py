while True:
  try:
    angka = int(input())
    for i in range(1,angka):
      print(str(i)*i, end= " ")
    break
  except ValueError:
    print("Maaf, Inputan hanya menerima angka")
  break