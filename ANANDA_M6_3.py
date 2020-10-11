# membuat dictionary kilas umur anak
kilasUmurAnak = {
    0 : [21, 15],
    1 : [17, 14],
    2 : [30, 21, 5],
    3 : [25, 23, 21, 19],
    4 : [17],
    5 : [6, 3],
    6 : [1, 12]
}

suspectUmurAtas = int(input("Suspect anak berumur (batas atas): "))
suspectUmurBawah = int(input("Suspect anak berumur (batas bawah): "))
suspectUrutan = int(input("Suspect anak lahiran ke-"))-1
print()

#membuat fungsi def 
def miripPolisi(keluarga):
    #menggunakan kondisi try except dengan try terdapat kondisi lagi berupa if elif else
    try:
        if kilasUmurAnak[keluarga][suspectUrutan] >= suspectUmurAtas or kilasUmurAnak[keluarga][suspectUrutan] <= suspectUmurBawah:
            print("di keluarga ke-"+str(keluarga+1,)+", anak lahiran ke-"+str(suspectUrutan+1), "tidak memenuhi kriteria tersangka")
            #Jika hasil dari value kilasUmurAnak[keluarga][suspectUrutan] lebih dari atau sama dengan suspect umur atas atau
            #kilasUmurAnak[keluarga][suspectUrutan] kurang dari sama dengan suspect umur bawah maka akan mengeluarkan output seperti keyword print diatas
            #dan jika kondisi if bernilai false, program akan menuju ke kondisi elif
        elif suspectUmurAtas>=kilasUmurAnak[keluarga][suspectUrutan]>=suspectUmurBawah:
            print("di keluarga ke-"+str(keluarga+1)+", anak lahiran ke-"+str(suspectUrutan+1), "berumur:", kilasUmurAnak[keluarga][suspectUrutan])
    except IndexError:
        print("[list index out of range] Pemilihan data keluarga untuk calon tersangka salah.")
        print("Jumlah anak dalam keluarga ke-", +int(keluarga+1), "tidak sesuai.")
        #Jika hasil inputan suspect tidak sesuai maka otomatis program akan menangkap kesalahan tersebut dan langsung mengeluarkan output except setelah if dan else pada kondisi try dilaksanakan
for keluarga in range(len(kilasUmurAnak)):
    miripPolisi(keluarga)
    #menggunakan looping for untuk mendeteksi apakah keluarga ada di dalam dictionary kilas umur anak
    #jika iya program akan terus melooping pada fungsi def yang telah dibuat