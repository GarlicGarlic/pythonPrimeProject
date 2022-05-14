def addPrime(pList, x, z):
  prime = True
  y = 0
  while primeList[y] < x**(0.5):
    y+=1
    if x%primeList[y] == 0:
      prime = False
      break
  if prime == True:
    pList.append(x)
  if x < 1000*z:
    addPrime(pList, x+2, z)
    return pList
  else:
    return pList

primeList = [2,3,5]

for i in range(1000):
  #print (i)
  primeList = (addPrime(primeList, (7+(1000*(i))), i+1))
print(primeList)
