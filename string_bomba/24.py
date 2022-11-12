q=input()
res = 0
while q == 1:

    if q != '0' and q != '1':
    
        if q == '\n':
            break
    
    res = res * 2 + (q - '0') 
    print( res/2, res/2, q, '0', res)  

print("Natija: ", res)

