def wordtolenmap(wordlist):
	return list(map(lambda x:len(x), wordlist))

print(wordtolenmap(['ab','cde','erty']))
