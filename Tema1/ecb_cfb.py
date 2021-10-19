import copy
import os
from Crypto.Cipher import AES


# generez un sir de 16 bytes
def generate_random_key(n):
    return os.urandom(n // 8)


# initializez iv ul pentru modul cfb
initialization_vector = generate_random_key(128)


# functie pentru a returna xor pe doua siruri de bytes
def byte_xor(x, y):
    return bytes([i ^ j for i, j in zip(x, y)])


# functie pentru decriptarea cu AES pentru fiecare mod de operare
def decrypt(mode, key, msg):
    result = b''
    if mode == "ecb":
        # impart mesajul primit pe blocuri de 16 octeti
        new_msg = [msg[i:i + 16] for i in range(0, len(msg), 16)]
        # preiau cifrul cu care voi decripta
        cypher = AES.new(key, AES.MODE_ECB)
        # pentru fiecare bloc de 16 octeti
        for mini_msg in new_msg:
            # decriptez fiecare bloc din cryptotext si il concatenez la rezultat
            result += cypher.decrypt(mini_msg)
    elif mode == "cfb":
        # preiau vectorul de initializare
        global initialization_vector
        # ii fac o copie
        aux = copy.deepcopy(initialization_vector)

        new_msg = [msg[i:i + 16] for i in range(0, len(msg), 16)]
        cypher = AES.new(key, AES.MODE_CFB, aux)
        for mini_msg in new_msg:
            # xor intre bloc si vectorul de initializare criptat
            xored_msg = byte_xor(mini_msg, cypher.encrypt(aux))

            # salvez blocul de plain text pentru urmatoarea iteratie
            aux = mini_msg

            result += xored_msg
    return result


# functie pentru criptarea cu AES pentru ecb si cfb
def encrypt(mode, key, msg):
    result = b''
    if mode == "ecb":
        new_msg = [msg[i:i + 16] for i in range(0, len(msg), 16)]
        cypher = AES.new(key, AES.MODE_ECB)
        for mini_msg in new_msg:
            # decritpez fiecare bloc pe rand
            result += cypher.encrypt(mini_msg)
    elif mode == "cfb":
        global initialization_vector
        aux = copy.deepcopy(initialization_vector)
        new_msg = [msg[i:i + 16] for i in range(0, len(msg), 16)]
        cypher = AES.new(key, AES.MODE_CFB, aux)
        for mini_msg in new_msg:
            xored_msg = byte_xor(mini_msg, cypher.encrypt(aux))
            # salvez blocul cryptotext pentru urmatoarea iteratie
            aux = xored_msg
            result += xored_msg
    return result
