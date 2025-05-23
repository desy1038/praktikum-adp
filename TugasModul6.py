#Fungsi untuk mengitung jarak
def distance(p1,p2):
    distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    return distance

#Input titik-titik
points = [[0,0] for i in range(3)]
for i in range(3):
    points[i][0] = float(input(f"masukkan x untuk titik ke-{i+1}:" ))
    points[i][1] = float(input(f"masukkan y untuk titik ke-{i+1}:" ))

#Hitung panjang sisi
a = distance(points[0],points[1])
b = distance(points[1],points[2])
c = distance(points[0],points[2])

#Menampilkan panjang sisi
print(f"panjang sisi a (titik 1 ke 2): {a}")
print(f"panjang sisi b (titik 2 ke 3): {b}")
print(f"panjang sisi c (titik 1 ke 3): {c}")

#Cek segitiga sama kaki
if a==b or b==c or a==c:
    print("Ketiga titik membentuk segitiga sama kaki")
else:
    print("Keitga titik  tidak membentuk segitiga sama kaki")
