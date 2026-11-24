



n=10
for i in range(1,n,2):
  for j in range(n-i):
    print("",end=" ")
    
  for k in range(i):
    print("*", end=" ")

  print()