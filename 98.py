ns,z = map(str,input().split())
z = int(z)
c =0
for i in range(z):
    if(str(i) in ns):
        c+=1
if(c == z):
    print("yes")
else:
    print("no")
