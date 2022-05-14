import math                         #import math
array=[]
A=0                                 #prime generator = 1
while A < 10001:                     #loop for while A is less than 100:
  prime=0                           #prime check = False
  A=A+1                             #prime generator = prime generator + 1
  B=A                               #possible prime = prime generator
  if B%2!=0 and B%3!=0:             #if possible prime is not a multiple of 2 or not a multiple of 3:
    C=3                             #unknown variable = 3
    while prime==0:                 #while prime check = False:
      C=C+2                         #unknown variable = unknown variable + 2
      if B%C==0:                    #if possible prime is not a multiple of unknown variable:
        prime=1                     #prime check = True
      elif C>math.sqrt(B):          #else if unknown variable is greater than the square root of possible prime:
        array.append(B)
        prime=1                     #prime check = True
print(array)
      
import math                      
A=10000                           #prime generator = 1
while A < 20000:                    #loop for while A is less than 100:
  rty=0
  prime=0                           #prime check = False
  A=A+1                             #prime generator = prime generator + 1
  B2=4*A+1+2*A*A                               #possible prime = prime generator
  # if B2%2!=0 and B2%3!=0 and B2%5!=0:
  for i in range (0, 100):
    if B2%array[i-1]!=0:
      rty=0; i=+1; continue                      #if possible prime is not a multiple of 2 or not a multiple of 3:
    else:
      rty=1; break
if rty==0:
  print(B2)
