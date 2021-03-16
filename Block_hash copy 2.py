import hashlib
import json
from time import time 

# Create Block
class Block():
    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = time()
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calhash()
        self.chain = []

# Create Hash Value through hashlib.sha256()
    def calhash(self):
        block_string = json.dumps({"nonce": self.nonce, " tstamp": self.tstamp, " transaction": self.transaction, " prevhash": self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
# Turn Ints into Strs Variables 
    def __str__(self):
        string= " nonce:" + " " + str(self.nonce) + "\n"
        string += " tstamp:" + " " + str(self.tstamp) + "\n"
        string += " transaction:" + " " + str(self.transaction) + "\n"
        string += " prevhash:" + " " + str(self.prevhash) + "\n"
        string += " hash:" + " " + str(self.hash) + "\n"

        return string 
# Print Hash Blocks
    def printHashes(self):
        print("prevhash", self.prevhash)
        print("hash", self.hash)

    def printBlock(self):
            """
                Print all of the data that's attached to the block
            """

            print("Index: " + str(self.nonce))
            print("Timestamp: " + str(self.tstamp))
            print("Data: " + json.dumps(str(self.transaction)))
            print("Previous Hash: " + str(self.prevhash))
            print("Hash: " + str(self.hash))

            print("\n")

# Create Blockchain 
class Blockchain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]

# Create the genesis block      
    def generateGenesisBlock(self):
        return Block(0, "" ," ", " ")

# Locate previous block
    def getLastBlock(self):
        return self.chain[-1]

# Add block chains together 
    def addBlock(self, new_block):
        new_block.prevhash=self.getLastBlock().hash
        new_block.hash=new_block.calhash()
        self.chain.append(new_block)

# Validate the blockchain 
    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevb=self.chain[i-1]
            currb=self.chain[i]
            if(currb.hash != currb.calhash()):
                print("invalid block")
                return False
            if(currb.prevhash != prevb.hash):
                print("invalid chain")
                return False
            return True


# Create an empty variable
quit = ""
# Create a empty dictionary 
block_chain={}
# Create a while loop
# Enter Sender/Receiver/Money Amount 
# Add to dictionary 
while quit != 'Quit':
        sender = input('Sender:')
        block_chain['Sender'] = sender
        receiver=input('Receiver:')
        block_chain['Receiver'] = receiver
        money_amt=input('Money_amt:')
        block_chain['money_amt']=money_amt
        quit=input("Enter Quit:")
print("Block Chain: ", block_chain)
# Print BlockChain
# Call instance of Block and Blockchain
B = Block(0, "", "", "")
BC = Blockchain()
# Add Chain 
BC.addBlock(Block(len(BC.chain), time(), block_chain))

# Create for loop that iterates through the chain

for my_block in BC.chain:
    my_block.printBlock()

# Call isChainValid()
# Determine  if block is valid 

Block_Valid = BC.isChainValid()
print(Block_Valid)
# Compares money amount and to it previous hash value
block_chain['money_amt'] = input('Enter Amount:')
print('Amount: ' , block_chain['money_amt'])

# Create another block with the updated amount
BC.addBlock(Block(len(BC.chain), time(), block_chain))
# Compare hash values and verify if hash value is valid. 
for my_block in BC.chain:
    my_block.printBlock()
Hash_block = BC.isChainValid()
print("Corrupted Hash Block: " , Hash_block)
if Hash_block == False:
        print("Invalid Hash Block")
 


