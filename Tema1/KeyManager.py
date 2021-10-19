import os
from ecb_cfb import encrypt


# generez un sir de 16 bytes
def generate_random_key(n):
    return os.urandom(n // 8)


class KeyManager:

    # initializez cheile in constructorul MC
    def __init__(self):
        self.initial_key = generate_random_key(128)
        self.k1 = generate_random_key(128)
        self.k2 = generate_random_key(128)
        self.k1 = encrypt("ecb", self.initial_key, self.k1)
        self.k2 = encrypt("cfb", self.initial_key, self.k2)

    # metode pentru a partaja cheia K pentru decriptarea cheilor k1 si k2
    def get_first_key(self):
        return self.initial_key

    # metoda pentru a partaja cheia k1
    def get_ecb_key(self):
        return self.k1

    # metoda pentru a partaja cheia k2
    def get_cfb_key(self):
        return self.k2
