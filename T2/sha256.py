import sys 
from Crypto.Hash import SHA256

def readFile(filePath):
    with open(filePath, 'rb') as f:
        f = f.read()
        return f

def blocks(binary):
    blocks = []
    for i in range(0,len(binary),1024):
        blocks.append(binary[i:i+1024])
    hashes = []
    blocks.reverse()

    h = SHA256.new(blocks[0])
    blockhash = h.copy()       
    hashes.append(blockhash)

    for i in range(1,len(blocks)):
        h = SHA256.new(blocks[i]) 
        h.update(blockhash.digest())
        blockhash = h.copy()
        hashes.append(blockhash.hexdigest())
    print(hashes[-1])

def main(file):
    binary = readFile(file)
    lista = blocks(binary)
data  = sys.argv
main(data[1])

# ~ python3 sha256.py FuncoesResumo\ -\ SHA1.mp4
# 302256b74111bcba1c04282a1e31da7e547d4a7098cdaec8330d48bd87569516
# ~ python3 sha256.py FuncoesResumo\ -\ Hash\ Functions.mp4
# 45013b3a2d5bc5369b90125da1dc55d2903c47c3852e13b04878df9942f21b9d