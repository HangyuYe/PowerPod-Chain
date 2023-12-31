import time
import threading
import json
from Crypto.Hash import keccak


class Block:
    def __init__(self, height, previous_hash, timestamp, data):
        self.height = height
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # 创建一个包含区块头数据的字典
        header = {
            'height': self.height,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
        }
        # 将字典转换为字符串
        header_string = json.dumps(header, sort_keys=True).encode()
        # 计算字符串的哈希
        return keccak.new(digest_bits=256, data=header_string).hexdigest()

    def __str__(self):
        return (f"Height: {self.height}\n"
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
        # Create the genesis block hash
        # Use Int 0 as the hash for the genesis block
        genesis_block_hash = keccak.new(digest_bits=256)
        genesis_block_hash.update((0).to_bytes(1, byteorder="big"))
        timestamp = int(time.time())
        block = Block(0, genesis_block_hash.hexdigest(), timestamp, "Genesis Block")
        print("Genesis Block Hash:", block.hash)
        return block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.chain.append(new_block)

    def schedule_block_addition(self):
        threading.Timer(30, self.auto_add_block).start() # Every 5 minutes, add a new block

    def auto_add_block(self):
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        timestamp = int(time.time())
        data = "0x0"
        new_block = Block(index, previous_hash, timestamp, data)
        self.add_block(new_block)
        print("New Block Added:")
        print(new_block)
        self.schedule_block_addition()  # Schedule the next block addition

