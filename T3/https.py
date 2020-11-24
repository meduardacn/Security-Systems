# -*- coding: utf-8 -*-
import sys
import hashlib
from Crypto.Cipher import AES

##################################################################
#### Etapa 1: Geração de chave usando Diffie-Hellman
##################################################################

#### Passo 1: gerar um valor a menor que p e calcular A = g**a mod p.
p = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCCA151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
g = "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5"
p = int(p, 16)
g = int(g, 16)
a = 1434365
#A = g**a % p
A = 4699796494490116413037673370996301481130361061910790885263408988759831217619840987371028799046440904418852271847520710936174645237010076551801572681483174312980194134517582620741382495864412633504299230456198887926681371870551779337105563800805208814190815801718196516197978553695425072509758802768451172976
print("A")
print("0%x" % A)
print("\n")
#### Passo 2: receber um valor B (em hexadecimal) e calcular V = B**a mod p
B = "585068BD6F89F4D5F0A870C1D88BE173FCFCB56437CDA4CAEBF1A5B3FAA5796F50BE88AE5A7A21928F2C4E02E79511113CBEE483976474C4C77FA64F45A4AD539F78EAA5B695CEA09290FC528EA09F7CA3CE0A520A21F70E2DD58F970B059B0760731F44B72870CC6ED76F66C51427276E6CB3912128E67C2B4956B5FDBF0975"
B = int(B, 16)
# V = B**a % p
V = 1545380011230707434797887121208013305455130481334383623322648210198749593783718824950829055165765299249585873499005947412217211291415565305028875735523670172897811919113171569736128141145553472296382911364914237490057222112091570665083183671645100501651333168184734887201786045416298717851682993001785748881
H = 1545380011230707434797887121208013305455130481334383623322648210198749593783718824950829055165765299249585873499005947412217211291415565305028875735523670172897811919113171569736128141145553472296382911364914237490057222112091570665083183671645100501651333168184734887201786045416298717851682993001785748881

#### Passo 3: calcular S = SHA256(V) e usar os primeiros 128 bits como senha para se comunicar com o professor.
# Si = bytes(str(V), 'utf-8')
# print(Si)
# Si = hashlib.sha256(Si).hexdigest().upper()[:32]    # V em int
# print(Si)
# print("\n")

# Sh = bytes(hex(V)[2:], 'utf-8')
# print(Sh)
# Sh = hashlib.sha256(Sh).hexdigest().upper()[:32]    # V em hex
# print(Sh)
# print("\n")

hexa = bytearray.fromhex("0%x" % V )
print(hexa)
Sba = hashlib.sha256(hexa).hexdigest().upper()[:32] # V em bytearray de hex
print(Sba)
print("\n")

##################################################################

##################################################################
#### Etapa 2: Troca de mensagens
##################################################################
# Receber uma mensagem (em hexadecimal), cifrada com o AES no modo de operação CBC, e padding. 
# Formato da mensagem recebida: [128 bits com IV][mensagem] – em hexadecimal.
msg = "E1DD68F3DF6E014DD50FCAE334CB63D1F0CA66608F48E38E9A40E31E9D266C985B708A5C106F3CC208083F547B19D9B2C5A9E4F5DAF2F5208FE3A1D3F01143D3A94DF90EA450C414FB1D127D9E1447A726B58E86CD7E81A089F59AC089A4771BD360EA54E14DC81E12A677DAB1A700CB"
msg = bytearray.fromhex(msg)

IV = msg[:32]
message = msg[32:]
print(IV)
print("\n")
print(message)


cipher = AES.new(Sba, AES.MODE_EAX, IV)
plaintext = cipher.decrypt(message)
print(plaintext)
# Decifrar a mensagem e mandar ela de volta ao professor cifrada e invertida (em hexadecimal), 
# ou seja, se receber “ola”, mandar de volta “alo”. 
# Formato da mensagem a ser enviada: [128 bits com IV aleatório][mensagem] – em hexadecimal.