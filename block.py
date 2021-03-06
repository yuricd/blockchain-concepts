from json import dumps
from hashlib import sha256


class Block:
    def __init__(self, index='', timestamp='', transactions=[], previous_hash='', nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def build_payload(self):
        return dumps(self.__dict__, sort_keys=True)

    def hash(self):
        payload = self.build_payload()
        return sha256(payload.encode()).hexdigest()

    def print(self):
        print(self.build_payload())
