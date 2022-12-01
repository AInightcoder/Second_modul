from math import factorial as fact

n = int(input("Son kiriting >>> "))

def n_chi_tub_son(n):
    count = 0
    
    for tub in range(2, 10**10):
        for r in range(2, 10**10):
            if tub%r==0 and tub!=r:
                break
            if tub%r==0 and tub==r:
                count+=1
                break
                
        if count==n:
            break

    return tub

def EKUB(a, b):
    while a!=0 and b!=0:
        if a>b:
            a%=b
        elif a<b:
            b%=a
        else:
            return 1
    return a+b

# print(fact(EKUB(n_chi_tub_son(n), n_chi_tub_son(n+10))))
print(n_chi_tub_son(n))