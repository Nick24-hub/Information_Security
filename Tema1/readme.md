# Tema 1
***
Securitatea Informatiei

### Descrierea mediului de lucru

Am ales sa folosesc limbajul Python deoarece pot face ceea ce fac in celelalte 
limbaje mai rapid si cu mai putin cod. Python are o multime de librarii ajutatoare
fiind recomandat si la optionalul de Introducere in Criptografie, in plus ca este
un limbaj ce trebuie obligatoriu invatat acum in anul 3.

Am folosit libraria cryptografica PyCryptodome pentru implementarea algoritmului 
de criptare AES fiind compatibila cu versiunile mai noi de Python.

Ca IDE am ales Pycharm deoarece imi este mai familair.

### Descrierea modului de rezolvare

Pentru reprezentarea nodurilor MC ( manager de chei ), A si B am folosit o clasa
pentru MC si o clasa pentru noduri din care am derivat obiectele A si B.
In initializarea nodului MC acesta isi genereaza in constructor cheile K,k1,k2
iar apoi am criptat cheile k1 si k2 folosind cheia K.

Noduirle A si B sunt legate de MC la initializare de la care extrag cheia K
iar cand apelez metoda de set_mode() acestea primesc k1 sau k2 in functie de
modul cerut ("ecb" sau "cfb"). Odata stabilit modul de operare pot apela 
metoda de send_message() pentru a trimite un mesaj de la nodul A la nodul B
in felul urmator: criptez plaintext-ul cu cheia corespunzatoare modului de operare,
B primeste cryptotext-ul pe care il decrypteaza cu ajutorul aceleiasi cheie
cu care a fost criptat obtinand plaintext-ul pe care il afiseaza in cele din urma.

Criptarea in modul ECB se realizeaza obtinand din aplicarea algoritmului
AES pe cheia k1 cifrul cu care criptez fiecare bloc de 16 octeti din plaintext
iar decriptarea se face la fel doar ca apelez metode de decriptare cu acelasi cifru.

Criptarea in modul CFB se realizeaz obtinand din aplicarea algoritmului AES
pe cheia k2 cifrul cu care criptez vectorul de initializare generat cu 16 octeti
in mod random iar apoi luand feicare bloc de plaintext la rand aplic xor intre
bloc si cifru salvand rezultatul pentru a-l utiliza la criptarea urmatorului bloc si concatenez
la cryptotext in acelasi timp.Decriptarea se realizeaza urmand aceiasi pasi
cu exceptia faptului ca de aceasta data se salveaza blocul curent pentru a-l folosi
la decriptarea urmatorului bloc.

### Testele efectuate pe diverse fisiere de intrare

Am testat programul pe doua fisiere de intrare, unul mai scurt si altul mai lung
iar ambele teste au trecut cu succes.

