N1=int(raw_input())
d=[]
for x in range(2,N1+1):
    if(N1%x== 0):
        if(x%2==0):
            d.append(x)
a=" ".join(map(str,d))
print(a)
