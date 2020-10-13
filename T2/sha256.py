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

    h = SHA256.new()
    h.update(blocks[0])
    blockhash = h.hexdigest()        
    binary = blockhash.encode()
    hashes.append(binary)
    for i in range(1,len(blocks)):
        block = blocks[i]+hashes[i-1]
        h = SHA256.new()
        h.update(block)
        blockhash = h.hexdigest()
        binary = blockhash.encode()
        hashes.append(binary)
    print(hashes[-1])
def main(file):
    binary = readFile(file)
    lista = blocks(binary)
data  = sys.argv
main(data[1])
