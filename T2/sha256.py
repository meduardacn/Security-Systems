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
    
        last = blocks[-1]
        blocks.pop()
        h = SHA256.new()
        h.update(last)
        print(h.hexdigest())

    

def main(file):
    binary = readFile(file)
    lista = blocks(binary)
data  = sys.argv
main(data[1])
