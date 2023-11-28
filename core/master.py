import time
import threading


class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __str__(self):
        return (f"Index: {self.index}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Hash: {self.hash}\n")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.schedule_block_addition()

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", time.time(), "Genesis Block", "somehash")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.chain.append(new_block)

    def schedule_block_addition(self):
        threading.Timer(60, self.auto_add_block).start()  # 600 seconds = 10 minutes

    def auto_add_block(self):
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        timestamp = time.time()
        data = f"Block {index} Data"
        hash = f"somehash{index}"
        new_block = Block(index, previous_hash, timestamp, data, hash)
        self.add_block(new_block)
        print("New Block Added:")
        print(new_block)
        self.schedule_block_addition()  # Schedule the next block addition


# Example usage
blockchain = Blockchain()

# The blockchain will now automatically add a new block every 10 minutes and print the block's information
