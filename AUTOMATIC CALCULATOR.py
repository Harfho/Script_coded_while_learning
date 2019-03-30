#created by Harfho 5-11-2 017bb


import time #import time
print('\n\n\t\t\t\t_____________AUTOMATIC CALCLULATOR________________')

prompt=str(input('\n\t\tselect :  \n\n\t\t d for division \n\t\t m for multiplication \n\t\t a for addition \n\t\t s for subtraction'.upper() +
		'\n\t\t E for exponential \n\t\t R for reminder \n\n\t\t C to quit \n \nselect : '.upper() )) #variable contain an input----whatever the user enter we be store int he variable

store=('\nYOU SELECT ')
#a variable 

while prompt.upper() != 'C':  #while loop we run until it become false
		
		if prompt.upper() == 'D' : #an if statement to check if what the user enter is equal to D 
									#if it is D the code below runs  if not it does not. 
				try: 

					print(store + 'division'.upper())
					ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
					ask_b=int(input('\nb = ')) #ask the user to input a number and store the number in this variable

					a=ask_a #store the number in variable ask_a into this variable
					b=ask_b #store the bumber in variable ask_b into this variable
					
					result_of_a_and_b= a / b # divide variable b from a  and store the result_of_a_and_b   
					print('\n' + str( a ) + ' divide by ' + str( b ) + ' = ',result_of_a_and_b) #print variable result_of_a_and_b
				
					prompt=input('\n\t\t\t(select again) or (enter \'c\' to exit): '.upper())

				except ValueError:
					print('\n invalid \'enter a number\'... '.upper())

		elif prompt.upper() == 'M': #an elif statement to check if what the user enter is equal to M 
									#if it is M the code below runs  if not it does not.

			
			try:

				print(store + 'multiplication'.upper())
				ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
				ask_b=int(input('\nb = ')) #ask the user to input a number and store the number in this variable

				a=ask_a #store the number in variable ask_a into this variable
				b=ask_b #store the bumber in variable ask_b into this variable
				
				result_of_a_and_b= a * b # multiply variable a and b and store the result_of_a_and_b   
				print('\n' + str( a ) + ' multiply by ' + str( b ) + ' = ',result_of_a_and_b) #print variable result_of_a_and_b
				prompt=input('\n\t\t\t(select again) or (\'c\' to cancel): '.upper()) #'''ask the user again if to select another operation or cancel(exit):whatever the user enter we affect the prompt at the beginning of this program '''

			except ValueError:
				
				print('\ninvalid \'enter a number\'... '.upper())
		
		elif prompt.upper() == 'A': #an elif statement to check if what the user enter is equal to A 
									#if it is A the code below runs if not it does not.

			
			try:

				print(store + 'addition'.upper())
				ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
				ask_b=int(input('\nb = ')) #ask the user to input a number and store the number in this variable

				a=ask_a #store the number in variable ask_a into this variable
				b=ask_b #store the bumber in variable ask_b into this variable
				
				result_of_a_and_b= a + b # Add up variable a and b and store the result_of_a_and_b   
				print('\n' + str( a ) + ' +  ' + str( b ) + ' = ',result_of_a_and_b) #print variable result_of_a_and_b
				prompt=input('\n\t\t\t(select again) or (enter \'c\' to exit): '.upper())#'''ask the user again if to select another operation or cancel(exit):whatever the user enter we affect the prompt at the beginning of this program '''

			except ValueError:
				print('\ninvalid \'enter a number\'... '.upper())
		
		elif prompt.upper() == 'S': #an elif statement to check if what the user enter is equal to  S 
									#if it is S the code below runs  if not it does not.

			try:
				print(store + 'subtraction'.upper())
				ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
				ask_b=int(input('\nb = ')) #ask the user to input a number and store the number in this variable

				a=ask_a #store the number in variable ask_a into this variable
				b=ask_b #store the bumber in variable ask_b into this variable
				
				result_of_a_and_b= a - b # subtract variable a from b and store the result_of_a_and_b   
				print('\n' + str( a ) + ' - ' + str( b ) + ' = ',result_of_a_and_b) #print variable result_of_a_and_b
				prompt=input('\n\t\t\t(select again) or (enter \'c\' to exit): '.upper()) #'''ask the user again if to select another operation or cancel(exit):whatever the user enter we affect the prompt at the beginning of this program '''

			except ValueError:
				print('\ninvalid \'enter a number\'... '.upper())

		elif prompt.upper() == 'R': #an elif statement to check if what the user enter is equal to  R 
									#if it is R the code below runs  if not it does not.

			try:
				print(store + 'reminder'.upper())
				ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
				ask_b=int(input('\nb = ')) #ask the user to input a number and store the number in this variable

				a=ask_a #store the number in variable ask_a into this variable
				b=ask_b #store the bumber in variable ask_b into this variable
				
				result_of_a_and_b= a // b # divide variable a from b and return the reminder,the reminder is then store in variable result_of_a_and_b   
				print('\n' + str( a ) + ' divide by ' +  str( b ) + ' we remain '+' = ',result_of_a_and_b) #print variable result_of_a_and_b
				prompt=input('\n\t\t\t(select again) or (enter \'c\' to exit): '.upper()) #'''ask the user again if to select another operation or cancel(exit):whatever the user enter we affect the prompt at the beginning of this program '''

			except ValueError:
				print('\ninvalid \'enter a number\'... '.upper())

		elif prompt.upper() == 'E': #an elif statement to check if what the user enter is equal to  E 
									#if it is E the code below runs  if not it does not.

			try:
				print(store + 'exponential'.upper())
				ask_a=int(input('\na = ')) #ask the user to input a number and store the number in this variable
				ask_b=int(input('\nround up to= ')) #ask the user to input a number and store the number in this variable

				a=ask_a #store the number in variable ask_a into this variable
				b=ask_b #store the number in variable ask_b into this variable
				
				result_of_a_and_b= a ** b # round up a to b 
				print('\n' + str( a ) + ' raise to power ' +  str( b ) + ' = ',result_of_a_and_b) #print variable result_of_a_and_b
				prompt=input('\n\t\t\t(select again) or (enter \'c\' to exit): '.upper()) #'''ask the user again if to select another operation or cancel(exit):whatever the user enter we affect the prompt at the beginning of this program '''

			except ValueError:
				print('\ninvalid \'enter a number\'... '.upper())

		else:
                    print('\nsorry no command for that!! '.upper())
                    prompt=input('\nselect again : '.upper())
time.sleep(0)
print('\n\n\nBYE..............THANKS.........FOR........USING..........MY..........PROGRAMME.........'.upper())
time.sleep(1)
print('\n\t\t\t\t\t\t__-------CREATE BY AFOLABI ROKEEB AKOLADE(----MHE-KAHN----)------__')
time.sleep(1)
print('\n\nhope you are satisfy with it'.upper())
input()
input()
input()
input('\n\n\t\t\t\tpress enter to exit .........'.upper())