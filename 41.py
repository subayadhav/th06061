a1,b=input().split()
c=0
for i in range(15):
    if int(b)**i==int(a1):
        c+=1
        break
if c==1:
    print("yes")
else:
    print("no")
