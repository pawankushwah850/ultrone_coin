class Miner:
    transactions = []

    def __init__(self):
        self.name = "pawan"

    @classmethod  # class method never access instance variable
    def add_transactions(cls, object):
        cls.transactions.append(object)

    @classmethod
    def display_transactions(cls):
        for each_transactions in cls.transactions:
            print(each_transactions.to_dict())
