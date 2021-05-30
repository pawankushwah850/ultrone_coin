from Lib import *


class Client:

    def __init__(self):
        random = Crypto.Random.new().read

        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signature = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        public_id = binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
        return public_id
