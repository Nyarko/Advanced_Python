number = int(input("Please type in the number: "))

def is_even():
	if number % 2 == 0:
		print ("True")

is_even()

print()

numbers = [1,56,234,87,4,76,24,69,90,135]

def is_even():
	for i in numbers:
		if i % 2 == 0:
			print (i)

is_even()

#lambda code for evens
numbers = [1,56,234,87,4,76,24,69,90,135]
evens = list(filter((lambda x: x % 2 == 0), numbers))
print ("\nThese are the evens: ")
print(evens)

#lambda code for odds
numbers = [1,56,234,87,4,76,24,69,90,135]
odds = list(filter((lambda x: x % 2 != 0), numbers))
print("\nThese are the odds: ")
print(odds)

#Not function code
numbers = [1,56,234,87,4,76,24,69,90,135]
odds = list(filter((lambda x: not (x % 2 == 0)), numbers))
print("\nThese are the odds: ")
print(odds)