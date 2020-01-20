def caesarCipher(str, key):
	alpha = list("abcdefghijklmnopqrstuvwxyz")
	str = list(str)
	newStr = []

	for i in range(len(str)):
		if str[i] == " ":
			newStr.append(str[i])
		else: 
			oldIdx = alpha.index(str[i])
			newIdx = (oldIdx + key) % 26
			newStr.append(alpha[newIdx])

	return "".join(newStr)		

print(caesarCipher("who is that", 1))