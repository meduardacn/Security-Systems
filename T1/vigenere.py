def keywordLength(chipherText, attempts):
	dic_ic = dict() # int -> [float] | possible keyword lenght -> [indexes of coincidence] 
	for i in range(1,attempts+1):	
		dic_ic[i] = []
		for j in range(i):	
			newText = ""
			k = j
			while k < len(chiperText):	
				newText += chiperText[k]
				k += i
			dic_ic[i].append(newText)
	return dic_ic		



def freq(chipherText):
	for elem in chipherText:
		value = listFreq[elem]
		listFreq[elem] = value + 1

icPT = 0.072723
listFreq = dict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0),
				 ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0),
				 ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), 
				 ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0),
				 ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)])


chiperText = input()

print( keywordLength(chiperText, 4) )


