str,n=map(str,input().split())
n=int(n)
length=len(str)
temp=str
for i in range(0,n):
	temp=temp[-1]+temp[:length-1]
print(temp)
