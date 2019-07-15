names = ["nana" , "papa" , "James"]
map(len, names)
print (list(map(len, names)))

def sqr(x): return x ** 2
map(sqr, map(len, names))
print (list(map(sqr, map(len, names))))

items = [1, 2, 3, 4, 5]
squars = map((lambda x: x ** 2), items)
print(list(squars))

def too_old(x): return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
filter(too_old, ages)
print (list(filter(too_old, ages)))

def too_young(x): return x < 30
filter(too_young, ages)
print (list(filter(too_young, ages)))