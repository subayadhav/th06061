ns=int(input())
l=[int(x) for x in input().split()]
t=0
if(ns==len(l)):
  for i in range(0,ns):
    for j in range(i+1,ns):
      t=l[i]^l[j]
print(t)      
