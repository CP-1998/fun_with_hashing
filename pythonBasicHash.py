import random
import hashlib


def hashFunction():
  hashList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            
  i = 0
  hashChoice = str()
  while i < 10:
    hashChoice += random.choice(hashList)
    i += 1
  hashInterim = hashChoice.encode('utf-8')
  hashFunc = hashlib.sha256()
  hashFunc.update(hashInterim)
  hashFinal = hashFunc.hexdigest()
  return(hashFinal)
  

test = hashFunction()

print(test)
