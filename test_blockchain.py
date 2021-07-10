from blockchain import Blockchain
from block import Block
import unittest
from json import dumps
from copy import deepcopy


index = 1
transactions = ['a', 'b']
timestamp = 'ts'
previous_hash = 'b'
proof = 100
sample_block = Block(index, transactions, timestamp, previous_hash, proof)


class TestBlockchain(unittest.TestCase):

    def last_block(self):
        pass

    def test_pow_success(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        computed_hash = blockchain.pow(block)

        self.assertEqual(blockchain.is_valid_proof(block), True,
                         'Should apply PoW algorithm successfully')

    def test_pow_failure(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        computed_hash = blockchain.pow(block)
        block.proof += 1
        self.assertEqual(blockchain.is_valid_proof(block), False,
                         'Should apply PoW algorithm and failed due to wrong proof counter')

    def test_is_valid_proof(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        block.proof = 6271  # proof for difficulty 3

        valid = blockchain.is_valid_proof(block, difficulty=3)

        self.assertEqual(valid, True,
                         'Should be valid')

    def test_add_new_transaction(self):
        pass

    def test_mine(self):
        pass


if __name__ == '__main__':
    unittest.main()
