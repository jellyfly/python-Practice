cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

# ok pay attention!
cities['_find'] = find_city

while True:
	print "State? (Enter to quit)",
	state = raw_input("> ")

	if not state: break

	# this line is the most important ever! study!
	city_found = cities['_find'](cities, state)
	# from the output we can tell that the function can also be as a variable in list
	print cities	# the output is : {'CA': 'San Francisco', 'MI': 'Detroit', 'NY': 'New York', '_find': <function find_city at 0x00000000023E1B38>, 'FL': 'Jacksonville', 'OR': 'Portland'}
	print city_found
	
