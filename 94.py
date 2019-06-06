ns=input()
c=0
for i in range(0,len(ns)):
    for j in range(i+1,len(ns)):
        if ns[i]==ns[j]:
            c=c+1
if c>=1:
    print("yes")
else:
    print("no")
