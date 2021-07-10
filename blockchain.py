from block import Block
import time


class Blockchain:
    def __init__(self):
        self.chain = [Block(index=0, transactions=[],
                            timestamp=time.time(), previous_hash=0)]
        self.unconfirmed_txs = []

    @property
    def last_block(self):
        return self.chain[-1]

    def pow(self, block, difficulty=3):
        proof_hash = block.hash()
        while not self.is_valid_proof(block, proof_hash, difficulty=difficulty):
            block.proof += 1
            proof_hash = block.hash()
        return proof_hash

    def add_block(self, block, proof_hash):
        previous_hash = self.last_block.hash()

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof_hash):
            return False

        self.chain.append(block)
        return True

    def is_valid_proof(self, block, proof_hash, difficulty=3):
        return block.hash().startswith('0' * difficulty) and block.hash() == proof_hash

    def add_transaction(self, transaction):
        self.unconfirmed_txs.append(transaction)

    def build_transaction(self, sender, receiver, amount):
        return dict(sender=sender, receiver=receiver, amount=amount)

    def mine(self):
        if not self.unconfirmed_txs:
            return False

        new_block = Block(index=self.index_1,
                          transactions=self.unconfirmed_txs,
                          timestamp=time.time(),
                          previous_hash=self.last_block.hash())

        proof_hash = self.pow(new_block)
        self.add_block(new_block, proof_hash)
        self.unconfirmed_txs = []
        return new_block.index

    def print(self):
        for block in self.chain:
            block.print()
