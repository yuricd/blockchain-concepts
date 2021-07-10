from block import Block
import time


class Blockchain:
    def __init__(self):
        self.chain = [Block(index=0, transactions=[],
                            timestamp=time.time(), previous_hash=0)]
        self.unconfirmed_tx = []

    @property
    def last_block(self):
        return self.chain[-1]

    def pow(self, block, difficulty=3):
        proof_hash = block.hash()
        while not self.is_valid_proof(block, difficulty=difficulty):
            block.proof += 1
            proof_hash = block.hash()
        return proof_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash()

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, difficulty=3):
        return block.hash().startswith('0' * difficulty)

    def add_new_transaction(self, transaction):
        self.unconfirmed_tx.append(transaction)

    def mine(self):
        if not self.unconfirmed_tx:
            return False

        last_block = self.last_block

        new_block = Block(index=self.index_1,
                          transactions=self.unconfirmed_tx,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        computed_hash = self.pow(new_block)
        self.add_block(new_block, computed_hash)
        self.unconfirmed_tx = []
        return new_block.index

    def print(self):
        for block in self.chain:
            block.print()


chain = Blockchain()
print(chain.print())
