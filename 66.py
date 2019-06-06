aa=list(map(int,input().split()))
z=aa[len(aa)-1]
a=[i for i in input().split()]
for i in a:
    if a.count(str(i))==z:
        print(i)
        break
