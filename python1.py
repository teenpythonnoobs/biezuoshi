
import os
import random
def sb(bb):
	if bb == 'scissor' :
		return 3
	elif bb == 'paper' :
		return 5
	elif bb == 'stone' :	
		return 4
	elif bb == 'exit' :
		return 6
	
win = False
ok=False
a=random.choice(['3','4','5'])
while not ok:
	bp=sb(input('put scissor paper stone\n'))
	
	
	if bp==6 :
		break
	if(bp==a):
		print("try	again")
		ok = True
	else:
		if (bp==5):
			if a==3:
				print("you	lose0")
				ok = True		
			elif a==4:
				print('you	win')
				win = True
		if (bp==4):
			if a==3:
				print("you	win")
				win = True
			elif a==5:
				print("you	lose")
				ok = True
		if  (bp==3):
			if a==4:
				print("you lose")
				ok = True
			elif(a==5):
				print("you win")
				win = True
		
	if win:
		againinputok=False
		while  not againinputok :
				yesorno=input("Do you want to play again? (y/n) \n")			
				if yesorno=="y" :
					ok=False
					againinputok = True		
				elif yesorno=="n" :
					ok=True
					againinputok = True
				else : 
					againinputok= False




