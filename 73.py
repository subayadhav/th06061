n1,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,len(l)):
	if l[i]==k:
		print(i+1)
		break
