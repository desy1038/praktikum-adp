#Cetak menu
def menu():
    print("\n" + "="*40)
    print("Selamat datang di Program Multifungsi")
    print("="*40)
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")


#Pilihan 1
def tabel_perkalian_modulo():
    while True:
        n = input("Masukkan nilai n (1 ≤ n ≤ 10): ")
        if n.isdigit():
            n = int(n)
            if 0 < n <= 10:
                break
            else:
                print("Nilai harus antara 1 hingga 10.")
        else:
            print("Input harus bilangan bulat positif.")
            
    print(f"\nTabel Cayley Modulo {n}:")

# Cetak header (judul kolom)
    print("   ", end="")  
    for i in range(n):
        print(f"{i:3}", end="")
    print()

    # Cetak isi tabel
    for i in range(n):
        print(f"{i:3}", end="")
        for j in range(n):
            hasil = (i * j) % n
            print(f"{hasil:3}", end="")
        print()

#Pilihan 2
def sigma_x():
    while True:
        bawah = input("Batas bawah: ")
        atas = input("Batas atas: ")
        if bawah.lstrip("-").isdigit() and atas.lstrip("-").isdigit():
            bawah = int(bawah)
            atas = int(atas)
            if atas >= bawah:
                break
            else:
                print("Batas atas harus lebih besar atau sama dengan batas bawah.")
        else:
            print("Masukkan bilangan bulat yang valid.")

    hasil = sum(range(bawah, atas + 1))
    print(f"Σ x = {hasil}")

#Pilihan 3
def faktorial():
    while True:
        n = input("Masukkan nilai n (n ≥ 0): ")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("Masukkan bilangan bulat ≥ 0.")

    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    print(f"{n}! = {hasil}")

# Pilihan 4
def total_dan_ratarata():
    while True:
        n = input("Masukkan banyak data (n > 0): ")
        if n.isdigit():
            n = int(n)
            if n > 0:
                break
            else:
                print("n harus lebih dari 0.")
        else:
            print("Masukkan bilangan bulat.")

    data = []
    for i in range(n):
        while True:
            x = input(f"Data ke-{i+1}: ")
            if x.replace('.', '', 1).replace('-', '', 1).isdigit():
                data.append(float(x))
                break
            else:
                print("Masukkan angka yang valid.")

def main():
    while True:
        menu()
        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            tabel_perkalian_modulo()
        elif pilihan == '2':
            sigma_x()
        elif pilihan == '3':
            faktorial()
        elif pilihan == '4':
            total_dan_ratarata()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

#Jalankan program
main()
                