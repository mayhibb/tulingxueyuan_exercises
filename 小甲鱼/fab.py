def fab():
    a = 0
    b = 1

    while a < 100:
        n = a
        a = b
        b = n + b
        print(a)
    else:
        return None
    

'''
a1 = 0, a2 = 1, An =a1 +a2 + a3 + a4 ..... + A(n-1)
'''

def qur():
    a = 0
    b = 1
    print(a)
    print(b)

    while a<10000:
        a = b
        b = a + b
        print(a)
    else:
        return None
    
