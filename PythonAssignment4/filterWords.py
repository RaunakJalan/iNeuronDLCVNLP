def filter_long_words(words_list,n):
	res = [x for x in words_list if len(x)>n]
	return res

print(filter_long_words(['hello','hi','you'],2))
