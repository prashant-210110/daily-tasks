n=7
for i in range(n):
  for j in range(n+1):
    if j==i or j==n-1-i:
      print("*",end="")
    else:
      print(" ",end="")
  print()
