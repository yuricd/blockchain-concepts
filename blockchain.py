from block import Block
import time


class Blockchain:
    def __init__(self):
        self._chain = [Block(index=0, timestamp=time.time(), transactions=[],
                             previous_hash=0)]
        self.unconfirmed_txs = []

    @property
    def last_block(self):
        return self._chain[-1]

    def pow(self, block, difficulty=3):
        proof_hash = block.hash()
        while not self.is_valid_proof(block, proof_hash, difficulty=difficulty):
            block.nonce += 1
            proof_hash = block.hash()
        return proof_hash

    def add_block(self, block, proof_hash):
        previous_hash = self.last_block.hash()

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof_hash):
            return False

        self._chain.append(block)
        return True

    def is_valid_proof(self, block, proof_hash, difficulty=3):
        return block.hash().startswith('0' * difficulty) and block.hash() == proof_hash

    def add_transaction(self, transaction):
        self.unconfirmed_txs.append(transaction)

    def build_transaction(self, sender, receiver, amount):
        return dict(sender=sender, receiver=receiver, amount=amount)

    def mine(self):
        if not self.unconfirmed_txs:
            return -1

        new_block = Block(index=self.last_block.index+1,
                          timestamp=time.time(),
                          transactions=self.unconfirmed_txs,
                          previous_hash=self.last_block.hash())

        proof_hash = self.pow(new_block)
        self.add_block(new_block, proof_hash)
        self.unconfirmed_txs = []
        return new_block.index

    def print(self):
        for block in self._chain:
            block.print()
