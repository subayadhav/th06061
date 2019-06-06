import math
n=int(input())
s=math.radians(n)
if(s>0 and s<1):
	print(round(math.sin(s),2))
else:
	print(round(math.sin(s)))
