#coding:utf-8
import random
number = random.randint(0, 10000)
'''print(number)'''
def IsRight(guessnumber,number,time):
	if guessnumber>10000 :
		print(' should smaller than 10000')
		return 0
	elif guessnumber<0 :
		print('should bigger than  than 0')
		return 0
	else:
		if guessnumber<number:
			print('smaller')
			return 0
		elif 	guessnumber>number:
			print('bigger')
			return 0
		else:
			
			print('you win!')
			return 1
			
		
ok = 0
message= 'input a number between 0 and 100000\n'
time=0
while (ok==0) :
	if time>14:
		print('you lose')
		ok=1
	else:
		inputs=input(message)
		try:
			guessnumber = int(inputs)
			if guessnumber is not None :
				if isinstance(guessnumber,int):
					time = time +1
					ok=IsRight(guessnumber,number,time)
					if ok==1:
						print('suceed in ' + str(time)+ ' time(s)')
				else :
					print("please input a number")
		except :
			if inputs=="exit":
				ok=1
			else:
				print("please input a number")
print('gameover')


