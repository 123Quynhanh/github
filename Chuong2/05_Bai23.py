import math
t=input('Nhap hai canh ke cua tam giac vuong:')
a=float(input())
b=int(input())
c=math.sqrt(a**2+b**2)
print('Canh ke thu nhat la:', a,end=',')
print(' canh ke thu 2:', b,end=',')
print(' co canh huyen =',round(c,2))