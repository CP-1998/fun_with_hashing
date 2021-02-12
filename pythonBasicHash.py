import random
import hashlib

hashList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


i = 0
hashChoice = str()
while i < 10:
  hashChoice += random.choice(hashList)
  i += 1
hashInterim = hashChoice.encode('utf-8')
hashFunc = hashlib.sha256()
hashFunc.update(hashInterim)
hashFinal = hashFunc.hexdigest()

  

print(hashFinal)

