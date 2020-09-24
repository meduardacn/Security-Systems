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

def unshiftLetter(letter):	
	# unshifted = 'a' - letter
    return 'z'

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
	key = ""
	for k, v in texts.items():	
		letter = mostFrequentLetter(v)
		key += unshiftLetter(letter)
	return key

def decrypt(chiperText):	
	keyWord = findKey(chiperText)
	clearText = ""
	for elem in chiperText:
		clearText += unshiftLetter(elem)
	print(clearText)


chiperText = input()
print("tamanho", len(chiperText))
decrypt(chiperText)
print("--- %s seconds ---" % (time.time() - start_time))
