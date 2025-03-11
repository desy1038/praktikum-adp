# Daftar harga paket
print("Daftar Paket Makanan :")
paket_ayam = 20000
print(f"Paket Ayam : {paket_ayam}")
paket_sapi = 35000
print(f"Paket Sapi : {paket_sapi}")
paket_cumi_cumi = 45000
print(f"Paket Cumi-cumi : {paket_cumi_cumi}")

pesanan = (input("pesanan paket : ")).lower()

# Harga paket
if pesanan == "paket ayam":
    harga = 20000
elif pesanan == "paket sapi":
    harga = 35000
elif pesanan == "paket cumi-cumi":
    harga = 45000
else:
    print("pilihan tidak valid!")

# Keterangan Pesanan

jumlah = int(input("jumlah pesanan anda : "))
total_harga = harga*jumlah

# ongkos kirim pesanan
jarak = float(input("jarak rumah anda dengan restoran (dalam km): "))

if jarak<1:
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else:
    ongkir = 15000

# hitung biaya total
total_biaya = harga + ongkir

# rincian pesanan
print(f"pesanan : {pesanan}")
print(f"harga paket : Rp{harga}")
print(f"ongkos kirim : Rp{ongkir}")
print(f"total biaya : Rp{total_biaya}")