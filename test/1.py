
son=12
son1=100

kattasi=0
kichigi=0
qoldiq=0

if son>son1:
  kattasi=son
  kichigi=son1
else:
  kattasi=son1
  kichigi=son

qoldiq=kattasi % kichigi 

if qoldiq!=0:

  kattasi=kichigi
  kichigi=qoldiq

  qoldiq=son % son1

print( "EKUB ", kichigi)

