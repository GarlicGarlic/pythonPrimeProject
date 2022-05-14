import math                       #import math
A=1800                            #prime generator = 1
while A < 200100:                    #loop for while A is less than 100:
  prime=0                           #prime check = False
  A=A+1                             #prime generator = prime generator + 1
  B=A                               #possible prime = prime generator
  if not B%2==0 and not B%3==0:      #if possible prime is not a multiple of 2 or not a multiple of 3:
    C=3                               #unknown variable = 3
    while prime==0:                   #while prime check = False:
      C=C+2                           #unknown variable = unknown variable + 2
      if B%C==0:                      #if possible prime is not a multiple of unknown variable:
        prime=1                         #prime check = True
      elif C>math.sqrt(B):            #else if unknown variable is greater than the square root of possible prime:
        print(B)                        #print possible prime
        prime=1                         #prime check = True
      
      
      
import math                      
A=1800                            #prime generator = 1
while A < 20100:                    #loop for while A is less than 100:
  prime=0                           #prime check = False
  A=A+1                             #prime generator = prime generator + 1
  B=4*A+1+2*A*A                               #possible prime = prime generator
  if B%7!=0 and B%7!=0 and B%7!=0 and B%7!=0 and B%7!=0 and B%7!=0:
    print(B)                      #if possible prime is not a multiple of 2 or not a multiple of 3:
