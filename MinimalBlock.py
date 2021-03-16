import hashlib
from time import *
from datetime import *
# Create Block Class 
class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()

    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8')) 
        key.update(str(self.timestamp).encode('utf-8')) 
        key.update(str(self.data).encode('utf-8')) 
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest() 

class MinimalChain():
    def __init__(self):
        self.blocks = [self.get_genesis_block()]
    
    def get_genesis_block(self):
        return MinimalBlock(0, datetime.utcnow(), 'Genesis', 'arbitrary')
    
    def add_block(self, data):
        self.blocks.append(MinimalBlock(len(self.blocks), datetime.utcnow(), data, self.blocks[len(self.blocks)-1].hash))
   

    def get_chain_size(self):
        return len(self.blocks)-1
    
    def verify(self, verbose=True):
        flag = True 
        for i in range(1, len(self.blocks)):
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i}.')
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous at block {i}.')
            if self.blocks[i-1].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Backdating at block{i}.')
        return flag

y = MinimalBlock(1, "3pm", "sender:Bob Recipent:Kev amount $3", "hash" )
y.hashing()
print(y.hashing())

x = MinimalChain()
x.get_genesis_block()
x.add_block("transaction")

print(x.get_genesis_block())
print(x.add_block("transaction"))
print(x.verify())
                


    