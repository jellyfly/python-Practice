d = {'a': 8.25, 'c': 2.87, 'b': 1.28, 'e': 12.49}
target = 3.19
key, value = min(dict.items(), key=lambda (_, v): abs(v - target))
print (key, value)
