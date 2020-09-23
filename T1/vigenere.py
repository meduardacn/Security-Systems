import time
start_time = time.time()

icPT = 0.072723

def newFrequencyDict():	
	return dict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0),
				 ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0),
				 ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), 
				 ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0),
				 ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)])

def keywordLength(chipherText, attempts):
	dic_ic = dict() 
	for i in range(1,attempts+1):	
		dic_ic[i] = []
		for j in range(i):	
			newText = ""
			k = j
			while k < len(chiperText):	
				newText += chiperText[k]
				k += i
			dic_ic[i].append(coincidenceIndexFor(newText))
	return dic_ic		

def coincidenceIndexFor(text):
    # first step -> char probability
	dictFreq = newFrequencyDict()
	for elem in text:
		dictFreq[elem] += 1
	ic = 0
	for k, v in dictFreq.items():	
		probability = ( v * (v-1)) / ( len(text) * (len(text)-1))
		ic += probability
	return round(ic,6)


chiperText = input()
print("tamanho", len(chiperText))
# print(coincidenceIndexFor(chiperText))
print( keywordLength(chiperText, 20))
print("--- %s seconds ---" % (time.time() - start_time))

