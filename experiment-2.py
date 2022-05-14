import math; A=7071050
while A < 7999999:
  prime=0; A+=1; B=4*A+1+2*A*A
  if not B%2==0 or not B%3==0:
    C=3
    while prime==0:
      C+=2
      if B%C==0:
        prime=1
      elif C>math.sqrt(B):
        print (B); prime=1
