sn,c=map(str,input().split())
count=0
for i in range(0,len(sn)):
	if(sn[i]==c):
		count+=1
	else:
		continue
print(count)
