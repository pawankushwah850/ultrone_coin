LAST_BLOCK_HASH = None


class Block:
    verified_transaction = []

    def __init__(self):
        self.previous_block_hash = None
        self.Nonce = None

    @classmethod  # class method never access instance veriable
    def add_transactions(cls, object):
        cls.verified_transaction.append(object)

    @classmethod
    def display_transactions(cls):
        for each_transactions in cls.verified_transaction:
            print(each_transactions.to_dict())
