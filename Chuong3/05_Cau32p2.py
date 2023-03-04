n=int(input('n='))
a=1
while a<=n and n>=1 and n<=50:
    print(a,end=' ')
    a=a+1
    while a%10==0:
        print(a)
        a=a+1
