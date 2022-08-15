t = int(input())
for i in range(t):
    n = int(input())
    print(f'#{i+1}')
    l=''
    for j in range(n):
        c,k=input().split()
        l+=c*int(k)
    for m in range(len(l)//10):
        print(l[0+10*m:10*(m+1)])
    if len(l)%10!=0:
        print(l[-(len(l)%10):])
    else:
        pass