aa=int(input())
l=[int(i) for i in input().split()]
t=[1 for i in range(aa) for j in range(i+1,aa) if l[i]<l[j]]
print(sum(t))
