from Crypto.Util.Padding import pad
from KeyManager import KeyManager
from Node import Node

# citesc mesajele din fisier
with open('msg_cbc.txt') as f:
    msg_cbc = f.read()

with open('msg_cfb.txt') as fl:
    msg_cfb = fl.read()

# ma asigur ca mesajele au lungimea divizibila cu 16
msg_cbc = pad(msg_cbc.encode(), 16)
msg_cfb = pad(msg_cfb.encode(), 16)

# creez obiectele intre care se realizeaza transferul de informatii
MC = KeyManager()
A = Node(MC)
B = Node(MC)

# setez modul de operare ecb
A.set_mode(MC, "ecb", B)

# trimit msg_cbc din nodul A in nodul B
A.send_message(msg_cbc, B)

print("\n")

# setez modul de operare cfb
A.set_mode(MC, "cfb", B)

# trimit msg_cfb din A in B
A.send_message(msg_cfb, B)
