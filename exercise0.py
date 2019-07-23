list=['li','wang','zhang','liu','dong']
print("guest:" + str(list))
list.remove('dong')
print(list)
print("\nanotherthree:")
list.insert(1,"rick")
list.insert(2,"morty")
list.append("birdperson")
print(list) 
'''
['li', 'rick', 'morty', 'wang', 'zhang', 'liu', 'birdperson' 
'''
print("\nI don't give a f**k," + list.pop(0))
print("\nI don't give a f**k," + list.pop(2))
print("\nI don't give a f**k," + list.pop(2))
print("\nI don't give a f**k," + list.pop(2))
print("\nok" + list[0] + list[1])
del list[:]
print(list)