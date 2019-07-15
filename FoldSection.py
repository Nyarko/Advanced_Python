from functools import reduce

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)
print()

words = ["hello", "world"]
added = '+'.join(words)
print (added)
def join_strings():
	final = reduce(lambda item, running_total: item + " " + running_total, words)
	return final
helloworld = join_strings() # "hello world"
print (helloworld)