def checkVowel(char):
	if char.isalpha() == False:
		return "Not a character"
	if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
		return "Vowel"
	return "Not vowel"

print(checkVowel('1'))
print(checkVowel('e'))
print(checkVowel('x'))

