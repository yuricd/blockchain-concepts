from blockchain import Blockchain
from block import Block
import unittest
from json import dumps
from copy import deepcopy

index = 1
transactions = ['a', 'b']
timestamp = 'ts'
previous_hash = 0
proof = 100
sample_block = Block(index, transactions, timestamp, previous_hash, proof)


class TestBlockchain(unittest.TestCase):

    def last_block(self):
        pass

    def test_pow_success(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        proof_hash = blockchain.pow(block)

        self.assertEqual(blockchain.is_valid_proof(block, proof_hash), True,
                         'Should apply PoW algorithm successfully')

    def test_pow_failure(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        proof_hash = blockchain.pow(block)
        block.proof += 1
        self.assertEqual(blockchain.is_valid_proof(block, proof_hash), False,
                         'Should apply PoW algorithm and failed due to wrong proof counter')

    def test_is_valid_proof(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)

        # proof for difficulty 3 in sample block
        proof_hash = blockchain.pow(block)

        valid = blockchain.is_valid_proof(block, proof_hash, difficulty=3)

        self.assertEqual(valid, True,
                         'Should be valid')

    def test_add_transaction(self):
        blockchain = Blockchain()
        new_tx = blockchain.build_transaction(
            'SenderAddress', 'ReceiverAddress', 10)

        self.assertEqual(blockchain.unconfirmed_txs, [],
                         'Should return empty unconfirmed transaction array')

        blockchain.add_transaction(new_tx)

        self.assertEqual(blockchain.unconfirmed_txs, [
                         new_tx], 'Should return 1 unconfirmed transaction in array')

    def test_add_block(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        block.previous_hash = blockchain.chain[0].hash()

        proof_hash = blockchain.pow(block)

        self.assertEqual(len(blockchain.chain), 1,
                         'Should return only genesis block before adding second block')

        was_added = blockchain.add_block(block, proof_hash)

        self.assertEqual(
            was_added, True, 'Should return true when add a valid block')

        self.assertEqual(len(blockchain.chain), 2,
                         'Should return only genesis block before adding second block')

    def test_mine(self):
        blockchain = Blockchain()
        block = deepcopy(sample_block)
        block.previous_hash = blockchain.chain[0].hash()

        proof_hash = blockchain.pow(block)

        self.assertEqual(len(blockchain.chain), 1,
                         'Should return only genesis block before adding second block')

        was_added = blockchain.add_block(block, proof_hash)

        self.assertEqual(
            was_added, True, 'Should return true when add a valid block')

        self.assertEqual(len(blockchain.chain), 2,
                         'Should return only genesis block before adding second block')


if __name__ == '__main__':
    unittest.main()
