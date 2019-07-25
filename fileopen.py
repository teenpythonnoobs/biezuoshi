with open('./test.txt') as file_object:
	thing=''.join(line.rstrip('\n') for line in file_object.readlines())

print(thing)

		
