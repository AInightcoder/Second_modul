with open("seventh.txt", 'r') as seventh:
    satr=seventh.read()
with open("seventh.txt", 'w') as seventh:  
    new_satr="Men oxirgi gapman"  
    seventh.write(new_satr +"\n"+ satr ) 
    