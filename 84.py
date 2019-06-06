ns=int(input())
l=list(map(int,input().split(" ")))
s=[]
for i in range(0,ns-1):
	s.append(l[i]|l[i+1])
print(max(s))	
