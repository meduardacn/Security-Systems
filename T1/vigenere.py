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
    # first step -> char probability
	dictFreq = newFrequencyDict()
	for elem in text:
		dictFreq[elem] += 1
	ic = 0
	for k, v in dictFreq.items():	
		probability = ( v * (v-1)) / ( len(text) * (len(text)-1))
		ic += probability
	return ic

def keywordLength(chipherText, attempts):
	dic_ic = dict() 
	dic_closerKey = dict()
	for i in range(1,attempts+1):	
		dic_ic[i] = []
		dic_closerKey[i] = []
		for j in range(i):	
			newText = ""
			k = j
			while k < len(chiperText):	
				newText += chiperText[k]
				k += i

			ic = coincidenceIndexFor(newText)
			if abs(icPT - ic) < 0.01:	
				print(i)
				return i 
	# 			tupla = (ic,abs(icPT-ic))
	# 			dic_closerKey[i].append(tupla)
	# 		dic_ic[i].append(ic)
	# #-------------------------------------------------------------
	# for k, v in dic_closerKey.items():	
	# 	if v != []:	
	# 		return k

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
	return letter

def findKey(chiperText):	
	lenght = keywordLength(chiperText,20)	
	texts = dict()
	for i in range(lenght):	
		newText = ""
		k = i
		while k < len(chiperText):	
			newText += chiperText[k]
			k += lenght
		texts[i] = newText
	shifts = []
	for k, v in texts.items():	
		letter = mostFrequentLetter(v)
		shifts.append(alphabet[letter])
	return shifts

def unshiftLetter(letter, shifts):	
	valueOfL = abs(alphabet[letter] + shifts)
	return alphabet[valueOfL%25]

def decrypt(chiperText):	
	shifts = findKey(chiperText)
	clearText = ""
	i = 0
	j = 0
	while i < len(chiperText):	
		key = shifts[j]
		letter = chiperText[i]
		clearText += unshiftLetter(letter,key)

		i += 1	
		j += 1	
		if j == len(shifts):	
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
chiperText = input()
print("tamanho", len(chiperText))
decrypt(chiperText)
print("--- %s seconds ---" % (time.time() - start_time))
