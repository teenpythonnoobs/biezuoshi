import random 
number = random.randint(0, 1000)
ok = 0

time=0
while (ok==0) :
	if time>14:
		print('you lose')
		ok=1
	else:
		inputs=input('input a number between 0 and 1000\n')
		try:
			guessnumber = int(inputs)
			if guessnumber is not None :
				if isinstance(guessnumber,int):
					time = time +1
					if guessnumber>1000 :
						print(' should smaller than 1000')
						ok= 0
					elif guessnumber<0 :
						print('should bigger than  than 0')
						ok= 0
					else:
						if guessnumber<number:
							print('smaller')
							ok= 0
						elif 	guessnumber>number:
							print('bigger')
							ok= 0
						else:
		
							print('you win!')
							ok= 1

					if ok==1:
						print('suceed in ' + str(time)+ ' time(s)')
						again=2
						while again==2 :
							yesorno=input("Do you want to play again? (y/n)")			
							if yesorno=="y" :
								ok=0
								time=0
								number = random.randint(0, 1000)
								again=0
							elif yesorno=="n" :
								again=1
							else :
								again=2
						ok=again
				else :
					print("please input a number")
		except :
			if inputs=="exit":
				ok=1
			else:
				print("please input a number")
print('gameover')