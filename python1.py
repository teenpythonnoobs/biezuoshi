import random



scissor=3
stone=4
paper=5
ok=0
a=random.choice(['3','4','5'])
while(ok==0):
	
		inputs=input('put scissor=3\paper=4\stone=5 ')
	
		if inputs == "EXit":
			ok==1
	
		else:
		
			if a==inputs:
				print("try again")
				ok==1
			elif a >inputs:
				if inputs==4:
			  		print("you lose")
				elif inputs==3 and a==5:	
					print('you win')
				elif inputs==3 and a==4:
					print("you lose")
					ok==1
			elif a <inputs:
				if inputs==5 and a==4:
					print("you win")
				elif inputs==5 and a==3:
					print ("you lose")
				elif inputs==4:
					print("you win")
					ok==1
		if ok==1:
			again=2
			while again==2 :
					yesorno=input("Do you want to play again? (y/n)")			
					if yesorno=="y" :
						ok=0
					elif yesorno=="n" :
						again=1
					else : 
						again=2
			ok=again
while again==2:
	print("gameover")  				  

	 													  
		  	
				
		  
	
