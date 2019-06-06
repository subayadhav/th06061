try:
	p1=int(input())
	if(p1>=-2**15+1  and p1<=2**15+1):
	    print ("INT")
	elif p1>=-2**31+1 and p1<=2**31+1:
	    print("LONG")  
	else:
	    print ("LONG LONG")
except ValueError:
	print("invalid")
