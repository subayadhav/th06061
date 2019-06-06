n2,r=map(int,input().split())
p=(n2//2)-1
for i in range(1,p+1):
  if i*p==r:
    print("yes")
    break
  else:
    p-=1
else:
  print("no")
