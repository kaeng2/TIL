n=int(input())
ls=map(int,input().split())
ls=sorted(ls)
print(ls[(n-1)//2])