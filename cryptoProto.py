import hashlib
import random
import datetime


# The SourceBloc class is the blueprint for the origin block, and all preceding blocks.
class SourceBloc:
  def __init__(self, hashData, dateTime, whereTo, whereFrom, nonce):
    self.hashData = hashData
    self.dateTime = dateTime
    self.whereTo = whereTo
    self.whereFrom = whereFrom
    self.nonce = nonce

# The createHash function will develop a unique hash for each block in the chain
  def createHash(self):
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
    return (hashFinal)

# Creates a unique timestamp at compilation to be attaced to the bloc object for verification
  def createTimestamp(self):
    today = datetime.datetime.now()
    return(today.strftime("%Y-%m-%d %H:%M:%S"))

# Asks user to declare wallet/place to send chain towards. All locations are to be entered alphanumerically.
  def senderFunction(self):
    sendTo = input ('Enter address: ')
    convertAddress = int(sendTo)
    return(convertAddress)

# Develops unique number for PoW mining, aka nonce
  def createNonce(self):
    num_list = [1, 1.5, 2, 2.2, 3, 3.7, 4, 4.1, 5, 5.2, 6, 6.6, 7, 7.9, 8, 8.3, 9, 9.5, 0, 0.5]

    i = 0
    hashChoice = int()
    while i < 5:
      hashChoice += random.choice(num_list)
      i += 1
    finalNonce = hashChoice * 2334 / 2
    return (finalNonce)


# Defines the source of the chain, not sure exactly if what I'm doing here will work but
  def homeFunction(self):
    home = 0
    return home

bloc = SourceBloc('', '', '', '', '')

bloc.whereTo = bloc.senderFunction()
bloc.whereFrom = bloc.homeFunction()
bloc.hashData = bloc.createHash()
bloc.dateTime = bloc.createTimestamp()
bloc.nonce = bloc.createNonce()

print('Sending to: ' + str(bloc.whereTo))
print('Sent From: ' + str(bloc.whereFrom))
print('Secure hash: ' + str(bloc.hashData))
print('Timestamp: ' + str(bloc.dateTime))
print('Nonce: ' + str(bloc.nonce))
