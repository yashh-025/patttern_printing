n=10
for i in range(n-1,0,-2):
  for j in range(n-1-i):
    print("",end=" ")
    
  for k in range(i):
    print("*", end=" ")

  print()