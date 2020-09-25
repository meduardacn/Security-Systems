import time

start_time = time.time()
icPT = 0.072723
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
	print("key length", largestLength)
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
	print(first, second)
	tuples = []
	for i in range(len(first)):	
		tuples.append([first[i],second[i]])	
	myprint(tuples,"")

keys = []

def myprint(vetor, palavra):	
	if vetor == []:
		return	

	if len(vetor) == 1:
		for i in vetor[0]:
    			keys.append(palavra+i)
			# print(palavra+i)
		return

	for i in vetor[0]:
		myprint(vetor[1:],palavra+i)


vetor =  [['1','2'],['3','4'],['5','6']] 
myprint(vetor,"")

def decrypt(cipherText, keyword):	
	clearText = ""
	i = 0
	j = 0
	print(keyword)
	while i < len(cipherText):	
		key = keyword[j]
		letter = cipherText[i]
		clearText += unshiftLetter(letter, key)
		i += 1	
		j += 1	
		if j == len(keyword):	
			j = 0
    		
	print(clearText)

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

cipherText = input()
print("tamanho", len(cipherText))
possibleKeys(cipherText)
decrypt(cipherText, "avelino")
print("--- %s seconds ---" % (time.time() - start_time))
