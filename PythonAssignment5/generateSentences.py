subjects = ["Americans","Indians"]
verbs = ["play","watch"]
objects = ["Baseball", "Cricket"]

sentences = [(sub + " " + verb + " " + ob + ".") for sub in subjects for verb in verbs for ob in objects]

for sent in sentences:
	print(sent)
