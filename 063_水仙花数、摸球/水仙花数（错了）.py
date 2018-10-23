# 1^3 + 2^3 + 3^3 = 36

ls = []
for m in range(1,10):
    for n in range(1,10):
        for k in range(1,10):
            i = (m*m*m + n*n*n + k*k*k)
            if 100<i<1000:
                ls.append(i)


ls = list(set(ls))
ls.sort()
print(ls)
                

    
