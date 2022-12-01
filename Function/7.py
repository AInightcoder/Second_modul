
def InvertDigit(son):
    son = int(son)
    reversed_num=0
    yangi_son=0

    while son>0:

        yangi_son=son%10
        reversed_num=reversed_num*10+yangi_son
        son=son//10
        
    return reversed_num


a=input("Enter: ")

print(InvertDigit(a))  