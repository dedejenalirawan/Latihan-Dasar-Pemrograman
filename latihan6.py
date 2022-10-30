print("===== Program Grade Nilai =====")
nilai = int(input("Inputkan nilai akhir: ")) 
if nilai >= 101:
    grade = "Nilai yang dimasukan berlebihan dan tidak ada dalam data"
    predikat = "Tidak ada dalam data" 
elif nilai >= 90:
    grade = "A"
    predikat = 'Dengan pujian'     
elif nilai >= 80:
    grade = "B"
    predikat = 'Sangat memuaskan'
elif nilai >= 70:
    grade = "C"
    predikat = 'Memuaskan'
elif nilai >= 60:
    grade = "D"
    predikat = 'Tidak memuaskan'
elif nilai <= -1:
    grade = "Nilai yang dimasukan tidak ada dalam data"
    predikat = 'Tidak ada dalam data'
else:
    grade = "E"
    predikat = "Tidak lulus"
print ("Grade Anda: %s" %grade)
print ("Predikat Anda: %s" %predikat)