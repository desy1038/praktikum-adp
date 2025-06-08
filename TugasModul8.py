#Input data praktikan
while True:
    jumlah_praktikan = int(input("masukkan jumlah praktikan (jumlah praktikan minimal 10): "))

    if jumlah_praktikan < 10:
        print("Jumlah praktikan harus minimal 10!")
    else:
        break

with open("data_praktikan.txt", "w") as f:
    for i in range(jumlah_praktikan):
        print(f"\nData ke_{i+1:}")
        nim = int(input("NIM : "))
        nama = input("Nama : ")
        pretest = int(input("Nilai Pretest : "))
        postest = int(input("Nilai Postest : "))
        tugas = int(input("Nilai Tugas : "))
        f.write(f"{nim},{nama},{pretest},{postest},{tugas}\n")

#baca file dan simpan ke dictionary
praktikan_dictionary = {}
with open("data_praktikan.txt","r") as f:
    for line in f:
        nim,nama,pretest,postest,tugas = line.strip().split(",")
        praktikan_dictionary[nim] = {
            "nama" : nama,
            "pretest" : int(pretest),
            "postest" : int(postest),
            "tugas" : int(tugas)
        }

#Hitung nilai akhir dan simpan ke file baru
nilai_akhir_dictionary = {}
with open("data_nilai_akhir.txt", "w") as f:
    f.write("Nim, Nama, Pretest, Postest, Tugas, Nilai Akhir\n")
    for nim, data in praktikan_dictionary.items():
        nilai_akhir = round(0.35 * data["pretest"] + 0.35 * data["postest"] + 0.30 * data["tugas"], 2)
        nilai_akhir_dictionary[nim] = nilai_akhir
        f.write(f"{nim},{data['nama']},{data['pretest']},{data['postest']},{data['tugas']},{nilai_akhir}\n")

#Analisis data nilai rata_rata
nilai_tertinggi = max(nilai_akhir_dictionary.values())
nilai_terendah = min(nilai_akhir_dictionary.values())
rata_rata = sum(nilai_akhir_dictionary.values()) / len(nilai_akhir_dictionary)
dibawah_rata = [nim for nim, nilai in nilai_akhir_dictionary.items() if nilai < rata_rata]

praktikan_nilai_tertinggi = [praktikan_dictionary[nim]['nama'] for nim, nilai in nilai_akhir_dictionary.items() if nilai == nilai_tertinggi]
praktikan_nilai_terendah = [praktikan_dictionary[nim]['nama'] for nim, nilai in nilai_akhir_dictionary.items() if nilai == nilai_terendah]

# menampilkan Hsil analisis
print("\n=== Hasil Analisis Nilai Praktikan ===")
print(f"Praktikan dengan Nilai Tertinggi: {nilai_tertinggi} oleh {', '.join(praktikan_nilai_tertinggi)}")
print(f"Praktikan dengan Nilai Terendah : {nilai_terendah} oleh {', '.join(praktikan_nilai_terendah)}")
print(f"Rata-rata Nilai Akhir Praktikan: {rata_rata:.2f}")
print(f"Jumlah praktikan di bawah rata-rata: {len(dibawah_rata)}")

if dibawah_rata:
    print("\n Daftar Praktikan dibawah Rata-rata : ")
    for nim in dibawah_rata:
        print(f"NIM: {nim}, Nama: {praktikan_dictionary[nim]['nama']}, Nilai Akhir: {nilai_akhir_dictionary[nim]}")