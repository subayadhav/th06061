a1=int(input())
b=0
for i in range(18):
    if 2**i==a1:
        b=1
        break
if b==1:
    print("yes")
else:
    print("no")
