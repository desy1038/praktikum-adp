x = [i for i in range (-7,8)]

f = []
for i in x:
    if i > 0:
       fungsi_x = x[i]**3 - x[i]
       f.append(fungsi_x)
    elif i < 0:
        fungsi_x = 1/x[i]**2
        f.append(fungsi_x)
    else:
        fungsi_x = 1
        f.append(fungsi_x)

print("| x | f(x) |")

for i in range(len(x)):
    print("|\t", x[i], "\t|\t", f[i], "\t|\t")