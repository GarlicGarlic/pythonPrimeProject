import math                                                                                 #import math
A=10000000                                                                                  #prime generator = 1
while A < 100000000:                                                                        #loop for while A is less than 100:
  prime=0                                                                                   #prime check = False
  A=A+1                                                                                     #prime generator = prime generator + 1
  B=A                                                                                       #possible prime = prime generator
  if not B%2==0 and not B%3==0 and not B%5==0 and not B%7==0 and not B%11==0:               #if possible prime is not a multiple of 2 or not a multiple of 3:
    C=11                                                                                    #unknown variable = 3
    while prime==0:                                                                         #while prime check = False:
      C=C+2                                                                                 #unknown variable = unknown variable + 2
      if C>math.sqrt(B):                                                                    #else if unknown variable is greater than the square root of possible prime:
        print(B)                                                                            #print possible prime
        prime=1                                                                             #prime check = True
      elif B%C==0:                                                                          #if possible prime is not a multiple of unknown variable:
        prime=1                                                                             #prime check = True
