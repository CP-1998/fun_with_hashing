import hashlib
import datetime
import secrets


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
    hashList = ['a', 'a', 'A', 'b', 'b', 'B', 'c', 'c', 'C', 'd', 'd', 'D', 'e', 'e', 'E', 'f', 'f', 'F', 'g', 'g', 'G', 'h', 'h' 'H', 'i', 'i' 'I', 'j', 'j', 'J',
                'k', 'k', 'K', 'l', 'l', 'L', 'm', 'm', 'M', 'n', 'n', 'N', 'o', 'o' 'O', 'p', 'p' 'P', 'q', 'q', 'Q', 'r', 'r', 'R', 's', 's', 'S', 't', 't', 'T',
                'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    i = 0
    hashChoice = str()
    while i < 256:
      hashChoice += secrets.choice(hashList)
      i += 1
    hashInterim = hashChoice.encode('utf-8')
    hashFunc = hashlib.sha256()
    hashFunc.update(hashInterim)
    hashFinal = hashFunc.hexdigest()
    return (hashFinal)

# Creates a unique timestamp at compilation to be attached to the bloc object for verification
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
    num_list = [ 1.5, 2.2, 3.7, 4.1, 5.2, 6, 6.6, 7, 7.9, 8.3, 9.5, 0.5]

    i = 0
    hashChoice = int()
    while i < 5:
      hashChoice += secrets.choice(num_list)
      i += 1
    finalNonce = hashChoice * 2334
    return (finalNonce)


# Defines the source of the chain, not sure exactly if what I'm doing here will work but...
  def homeFunction(self):
    home = 0
    return home



# A new instance of SourceBloc is being created to play around with. I eventually will create a self.function to build new SourceBloc
# objects, which will inherit the SourceBloc blueprint but will add the previousHash function to verify the legitimacy of the sent
# data. I have a lot to learn before proceeding to this point however.

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