import time

start_time = time.time()
icPT = 0.072723

def leitura(txt):#leitura e tratamento da entrada txt
	f = open(txt, 'r')
	f = f.read() #Leitura do Arquivo
	print(f)
	
	#return list_op

def newFrequencyDict():	
	return dict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0),
				 ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0),
				 ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), 
				 ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0),
				 ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)])

def coincidenceIndexFor(text):
	dictFreq = newFrequencyDict()
	for elem in text:
		dictFreq[elem] += 1
	ic = 0
	for k, v in dictFreq.items():	
		probability =  v * (v-1)
		ic += probability
	return (ic / ( len(text) * (len(text)-1)))

def keywordLength(chipherText, attempts):
	dic_ic = dict() 
	for i in range(1,attempts+1):	
		dic_ic[i] = []
		for j in range(i):	
			newText = ""
			k = j
			while k < len(cipherText):	
				newText += cipherText[k]
				k += i

			ic = coincidenceIndexFor(newText)
			dic_ic[i].append(ic)
	#-------------------------------------------------------------
	largestIC = 0 
	largestLength = 0 
	for k, v in dic_ic.items():	
		average =  0
		for elem in v:	
			average += elem
		average = average/len(v)
		if average > largestIC:	
			largestIC = average
			largestLength = k
	newFile.write("key length:"+ str(largestLength) + "\n")
	return largestLength
		
def mostFrequentLetter(text):	
	dictFreq = newFrequencyDict()
	for elem in text:
		dictFreq[elem] += 1
	letter = ""
	biggerFreq = 0
	for k, v in dictFreq.items():	
		if v > biggerFreq:	
			letter = k
			biggerFreq = v
	
	dictFreq[letter] = 0
	biggerFreq = 0
	sletter = ""
	for k, v in dictFreq.items():	
		if v > biggerFreq:	
			sletter = k
			biggerFreq = v

	return (letter, sletter)

def findKey(cipherText):	
	lenght = keywordLength(cipherText,20)	
	texts = dict()
	for i in range(lenght):	
		newText = ""
		k = i
		while k < len(cipherText):	
			newText += cipherText[k]
			k += lenght
		texts[i] = newText
	mostFrequent = ""
	secondMost = ""
	for k, v in texts.items():	
		f, s  = mostFrequentLetter(v)
		mostFrequent += f
		secondMost += s
	return(mostFrequent, secondMost)

def unshiftLetter(letter, key):	
	valueOfL = alphabet[letter] - alphabet[key]
	return alphabet[valueOfL%26]

def possibleKeys(cipherText):	
	first, second = findKey(cipherText)
	newFile.write("------------------------------------------------------------------------------------------------------------\n")

	newFile.write("The most frequent letters and the second largest ones,respectively: " + first + " and " + second + "\n")
	newFile.write("------------------------------------------------------------------------------------------------------------\n")
	
	array = [first,second]
	myprint(array,"")
	keysList = list(keys)
	newFile.write("These are all the possibilities of keys using the two words with the most frequent letters: \n")
	for elem in keysList:	
		newFile.write(elem + "\n")

keys = set()
def myprint(vetor, palavra):	
	if vetor == []:
		return
	if len(vetor[0]) == 1:
		for i in vetor:	
			keys.add(palavra+i)
			# print(palavra+i)
		return
	aux = []
	for i in vetor:
		aux.append(i[1:])
	for i in vetor:
		myprint(aux,palavra+i[0])

def decrypt(cipherText, keyword):	
	clearText = ""
	i = 0
	j = 0
	while i < len(cipherText):	
		key = keyword[j]
		letter = cipherText[i]
		clearText += unshiftLetter(letter, key)
		i += 1	
		j += 1	
		if j == len(keyword):	
			j = 0	
	return clearText		

alphabet = dict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4),
				 ('f', 5), ('g', 6), ('h', 7), ('i', 8), ('j', 9),
				 ('k', 10), ('l', 11), ('m', 12), ('n', 13), ('o', 14), 
				 ('p', 15), ('q', 16), ('r', 17), ('s', 18), ('t', 19),
				 ('u', 20), ('v', 21), ('w', 22), ('x', 23), ('y', 24), ('z', 25),
				 (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'),
				 (5, 'f'), (6, 'g'), (7, 'h'), (8, 'i'), (9, 'j'),
				 (10, 'k'), (11, 'l'), (12, 'm'), (13, 'n'), (14, 'o'), 
				 (15, 'p'), (16, 'q'), (17, 'r'), (18, 's'), (19, 't'),
				 (20, 'u'), (21, 'v'), (22, 'w'), (23, 'x'), (24, 'y'), (25, 'z')])

print("------------------------------------------------------------------------------------------------------------")
print("Enter file path with encoded text:")
file = input()
print("------------------------------------------------------------------------------------------------------------")
f = open(file, "r")
cipherText = f.read()
f.close()

x = file.split('/')
name = x[-1]

open("results/"+name, "w").close()
newFile = open("results/"+name, "a")

possibleKeys(str(cipherText))
newFile.write("Time to find all possible keys: %s seconds" % (time.time() - start_time))
newFile.write("\n------------------------------------------------------------------------------------------------------------\n")

print("All possible keyword was created in the file", name, "choose one to decrypt the text")
print("------------------------------------------------------------------------------------------------------------")
newFile.close()

newFile = open("results/"+name, "a")
print("Insert the keyword:")
print("------------------------------------------------------------------------------------------------------------")
keyword = input()
start_time = time.time()
result = decrypt(cipherText, keyword)
newFile.write("\n" + result + "\n")
newFile.write("\nTime to decrypt text: %s seconds" % (time.time() - start_time))
newFile.close()