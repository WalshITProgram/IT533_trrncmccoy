import hashlib
import json
from time import time
# Create Blockchain class 
class Blockchain(object):
    def __init__(self):
        # Create a chain with a empty list that well add blocks 
        self.chain = []
        # When users send a coin to each other transactions will sit in this array until we approve
        self.pending_transactions = []
        # Add each block to chain 
        self.new_block(previous_hash="James will be here", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof, 
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1
    
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", "10 BTC")
t2 = blockchain.new_transaction("John", "Bryant", "20 BTC")
t3 = blockchain.new_transaction("Lamelo", "Ball", "30 BTC")
blockchain.new_block(12345)

t1 = blockchain.new_transaction("Michael", "Jordan", "100 BTC")
t2 = blockchain.new_transaction("Cam", "Newton", "200 BTC")
t3 = blockchain.new_transaction("Kevin", "Garnett", "300 BTC")
blockchain.new_block(6789)

print("Genesis block:", blockchain.chain)


