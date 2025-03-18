
lanjut = True

while lanjut:
    angka_1 = float(input("Masukkan angka pertama: "))
    angka_2 = float(input("Masukkan angka kedua (Jika pembagian tidak boleh 0): "))
    print("""
    PILIHAN OPERASI
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Keluar
    """)
    opsi = input("Masukkan operasi: ")

    if opsi == "1":
        hasil = angka_1 + angka_2
        print(hasil)
    elif opsi == "2":
        hasil = angka_1 - angka_2
        print(hasil)
    elif opsi == "3":
        hasil = angka_1 * angka_2
        print(hasil)
    elif opsi == "4":
        if angka_2 == 0:
            print("Angka kedua tidak boleh 0")
        else:
            hasil = angka_1 / angka_2
            print(hasil)
    elif opsi == "5":
            break
    else :
        print("Pilih operasi yang tersedia")