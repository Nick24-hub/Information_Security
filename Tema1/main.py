from Crypto.Util.Padding import pad
from KeyManager import KeyManager
from Node import Node

# citesc mesajele din fisier
with open('msg1.txt') as f:
    msg1 = f.read()

with open('msg2.txt') as fl:
    msg2 = fl.read()

# ma asigur ca mesajele au lungimea divizibila cu 16
msg1 = pad(msg1.encode(), 16)
msg2 = pad(msg2.encode(), 16)

# creez obiectele intre care se realizeaza transferul de informatii
MC = KeyManager()
A = Node(MC)
B = Node(MC)

# setez modul de operare ecb
A.set_mode(MC, "ecb", B)

# trimit mesajele din nodul A in nodul B
A.send_message(msg1, B)
print("\n")

A.send_message(msg2, B)
print("\n")

# setez modul de operare cfb
A.set_mode(MC, "cfb", B)

A.send_message(msg1, B)
print("\n")

A.send_message(msg2, B)
print("\n")
