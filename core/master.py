class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", "01/01/2020", "Genesis Block", "somehash")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.chain.append(new_block)


# Example usage
blockchain = Blockchain()
blockchain.add_block(Block(1, blockchain.get_latest_block().hash, "01/02/2020", "Block 1 Data", "somehash1"))
blockchain.add_block(Block(2, blockchain.get_latest_block().hash, "01/03/2020", "Block 2 Data", "somehash2"))

# Display the blockchain
for block in blockchain.chain:
    print(f"Block {block.index}: {block.data}")
