from Crypto.Util.Padding import unpad
from ecb_cfb import decrypt, encrypt


class Node:

    # initializez un nod cu legatura la key manager
    def __init__(self, key_manager):
        self.mode = ""
        self.initial_key = key_manager.get_first_key()
        self.key = "".encode()

    # metoda care extrage cheia corespunzatoare modului cerut de la key manager dupa care o decripteaza si o partajeaza
    def set_mode(self, key_manager, mode, other_node):
        if mode == "ecb":
            self.mode = "ecb"
            self.key = key_manager.get_ecb_key()
            self.key = decrypt(self.mode, self.initial_key, self.key)
            other_node.mode = "ecb"
            other_node.key = self.key
        elif mode == "cfb":
            self.mode = "cfb"
            self.key = key_manager.get_cfb_key()
            self.key = decrypt(self.mode, self.initial_key, self.key)
            other_node.mode = "cfb"
            other_node.key = self.key

    # metoda pentru a cripta un mesaj si a-l trimite mai departe unui nod
    def send_message(self, plain_text, receiver_node):
        crypto_text = encrypt(self.mode, self.key, plain_text)
        print("Sent message: " + str(crypto_text))
        receiver_node.receive_message(crypto_text)

    # metoda pentru a decripta un mesaj primit dupa care il afiseaza
    def receive_message(self, crypto_text):
        print("Received message: " + str(crypto_text))
        plaintext = decrypt(self.mode, self.key, crypto_text)
        print("Received message after decrypt: " + str(unpad(plaintext, 16)))
