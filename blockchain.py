from records import *
import hashlib

# Block class that stores the hash value that is representative of the block data.
# The block data is comprised of the previous block's hash value and the current 
# transactions being added to the current block.
class Block:
    def __init__(self, prev, trans_list) -> None:
        self.previous_block = prev
        self.transaction_list = trans_list
        self.data = self.previous_block + "," + ",".join(self.transaction_list)
        self.hash_val = hashlib.sha256(self.data.encode()).hexdigest()
        
class Blockchain(Record): 
    def __init__(self, path = "/cache/chain.txt", bList = [], *blocks) -> None:
        super().__init__(path, bList, *blocks)