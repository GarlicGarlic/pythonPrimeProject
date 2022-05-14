lis=[]
primeList=[]
import math


def n(possiblePrime):
  for i in range (len(lis)):
    prime2=int(lis[i])
    if prime2<possiblePrime:
      if possiblePrime%prime2==0:
        return False
  return True

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
        lis.append(B)
        prime=1                     #prime check = True
  

for A in range (len(lis)):
  B=4*A+1+2*A*A
  if n(B)==True:
    primeList.append(B)
print(lis)
print(primeList)
