ns=int(input())
l=[int(i) for i in input().split()]
for i in range(0,ns-1,2):
	l[i],l[i+1]=l[i+1],l[i]
print(*l)
