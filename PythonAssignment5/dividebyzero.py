a=5
b=0
test=0
try:
	test = a/b
	print(test)
except Exception as e:
	print(e)
finally:
	print("Done Execution.")
