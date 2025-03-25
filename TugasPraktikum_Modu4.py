n = int(input("masukkan jumlah baris yang akan dicetak (minimal 4) : "))

if n%2==0:
    d = int(n/2)
    for i in range (1, d+1):
        print(" BOOM " * (i-1) + " 1 " + " BOOM " * (n-2*i) + " 2 " + " BOOM " * (i-1))
    for i in range (1, d+1): 
        print(" BOOM " * (d-i) + " 2 " + " BOOM " * (2*i-2) + " 1 " + (d-i) * " BOOM ")
else:
    t = int(n//2)
    for i in range (1,t+1):
         print(" BOOM " * (i-1) + " 1 " + " BOOM " * (n-2*i) + " 2 " + " BOOM " * (i-1))
    print(" BOOM " * t + " HORE " + " BOOM " * t)
    for i in range (1, t+1):
        print(" BOOM " * (t-i) + " 2 " + " BOOM " * (2*i-2) + " 1 " + (t-i) * " BOOM ")

counter_boom = n**2 - ((n-1)*2+1)

print(f"Jumah BOOM adalah sebanyak {counter_boom}")
