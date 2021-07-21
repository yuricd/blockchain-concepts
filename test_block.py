from block import Block
import unittest
from json import dumps

index = 1
transactions = ['a', 'b']
timestamp = 'ts'
previous_hash = 'b'
nonce = 100
new_block = Block(index, transactions, timestamp, previous_hash, nonce)


class TestBlock(unittest.TestCase):
    def test_build_payload(self):
        payload = new_block.build_payload()
        expected = dumps(dict(index=index, nonce=nonce, previous_hash=previous_hash,
                         timestamp=timestamp, transactions=transactions), sort_keys=True)
        self.assertEqual(payload, expected, 'Should match dicts')

    def test_hash(self):
        generated_hash = new_block.hash()
        self.assertEqual(len(generated_hash), 64, 'Should match hash')


if __name__ == '__main__':
    unittest.main()
