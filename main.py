from Miner import Miner
from Client import Client
from Transcation import Transaction
from Block import Block

COINS = []

miner = Miner()

pawan = Client()
monk = Client()
admin = Client()
nora = Client()

t1 = Transaction(pawan, monk.identity, 10)
t2 = Transaction(monk, pawan.identity, 30)
t3 = Transaction(admin, monk.identity, 90)
t4 = Transaction(nora, admin.identity, 6)

t5 = Transaction(pawan, nora.identity, 10)
t6 = Transaction(monk, pawan.identity, 60)
t7 = Transaction(nora, pawan.identity, 90)
t8 = Transaction(nora, monk.identity, 96)

t1.sign_transaction()
t2.sign_transaction()
t3.sign_transaction()
t4.sign_transaction()

t5.sign_transaction()
t6.sign_transaction()
t7.sign_transaction()
t8.sign_transaction()

block0 = Block()
block1 = Block()

block0.add_transactions(t1)
block0.add_transactions(t2)
block0.add_transactions(t3)
block0.add_transactions(t4)

block1.add_transactions(t5)
block1.add_transactions(t6)
block1.add_transactions(t7)
block1.add_transactions(t8)

digest = hash(block0)
last_block_hash = digest

digest2 = hash(block1)
last_block_hash = digest2

COINS.append(block0)
COINS.append(block1)

for obj in COINS:
    obj.display_transactions()
    print()

# miner.add_transactions(t1)
# miner.add_transactions(t2)
# miner.display_transactions()
