import random
import time



print('\t\t\t\t!!!-------------------------!!!')
print('\n\t\t\t\t guess the secret number game'.upper())
print('\n\t\t\t\t!!!-------------------------!!!')

print('\n-------------------------------------wait------------------------------------------------'.upper())

print('\nloading.........................................................................................'.upper())

print('\n\n\t----------------------------------------------------------------------------------------------------')

info=('\n\n\t\t\tthis is a guessing game where by computer store a secret number and hide it ...'.upper() +
      '\n\n\t\t\tso you are to pridict the hiding number...........'.upper() + 
      '\n\n\t\t\tif you pridict it right you we be awarded  5  point(),'.upper() +
      '\n\n\t\t\tif fail you we lose 1 point()....'.upper())

print(info)
print('\n\t-------------------------------------------------------------------------------------------------------')
input('\n\t\t\t......press enter key to continue..........')
print('\n\n\t---------------------------------------------------------------------')
print('\n\t\t(you have already be given 20 point) '.upper() +
      '\n\n\t\ttry has much has possible to increase your point to 100'.upper()) 
print('\n\t-----------------------------------------------------------------------------------------------------')

input('\n\t\t\t......press enter key to continue..........'.title())

print('\n\n\t\t___________________________________----TO QUIT-----_____________________________')

print('\n\t\t------type (exit) or (q)------'.upper())

print('\t\t__________________________________________________________________________________________')
input('\n\n\t\t\tto start the game press enter'.upper())

print('\n\n\n\n------------------------------------------------------------------------------------------------')
print('\n\n\t\tto make the game fun i have include a (help) prompt at some places '.upper() +
    '\n\n\n\t\t\tso has to keep you in touch with the number the computer hide. '.upper())
print('-----------------------------------------------------------------------------------------------')
print('\n\n\n\n\n\t\t\t__________------GOOD-Lucky------______________'.upper())

mess = '\nwhat is the secret number : '.upper()
try_again = "did you what to play again ".upper()
exqt = True
point=20
trial=0
retype=('\nretype your name : '.upper())
name=input('\n\nbefore we start what is your name : '.upper())
names=name.lower()
check=input(retype)
namess=check
active=True
while active:
    if str(namess).lower() == names:

        print('\n\n\t\t\t\t\tsuccessful'.upper())
        print('\n\n\t\t\t\t' + names.upper() +' is given = '.upper() + str(point) + ' point')
        
        def game():
            global exqt
            global mess
            global try_again
            global point
            global guess
            global help_
            global trial
            while exqt:
                
                guess = random.randint(0,100)    
                help_=guess-2
                
                # print('\n\nhelp' + str(help_))
                stor = input(mess)
                c_guess = stor
                print('\nhelp '.upper() + str(guess))
                trial +=1
                # print('\n\n\nhelp' + str(help_))

                


                if str(stor).lower() != 'exit':
                    if str(stor).lower() != 'q':
                        try:
                            if int(stor) < guess:
                                
                                point -= 1

                                print('\n\n\t\t\t too low guess again'.upper())
                                print('\n\t\t\tyour point ='.upper() ,point)
                                


                            elif int(stor) > guess:
                                point-=1
                                print('\n\n\t\ttoo high. guess again'.upper())
                                print('\n\t\t\tyour point ='.upper() , point)
                                print('\ndont forget to enter (q) or (exit) when  u are done'.upper())
                            elif int(stor) == guess:   
                                point += 10
                                print("\n\tyou guess ".upper() + 'it'.upper() + ' right.'.upper() +
                                      "\n\t computer secret number = ".upper() + c_guess +
                                      "\n\t your guess number = ".upper() + c_guess)
                                print('\n\t\t\tyour point is now ['.upper()+ str(point) + '] point'.upper())
                        except ValueError:
                            print("\t\t\tEnter a Value please.........".upper())

                    elif not exqt :
                        exqt=False 
                    else:
                         exqt=False

                else :
                     exqt=False


        game()
        exqt_defult= exqt=True

        print('\n\n\n\n\n\n\t\t ' + names  + '___________your total point  = '.upper() + '[' + str(point) + ']')
        print('\n\t\t\t\t\t '+ names +' -----------------all your trial = '.upper() + str(trial-1) + ' ------------------' )
        print("Bye,play back later__".upper())




        prompt=input('\n\nenter (r) to play again or press enter to exit '.upper() + 
            '\n---------------------------------------Notice---------------------------- if u enter'.upper() + 
            '(q) or (exit) after re_playing '.upper() +
            'the game'.upper() + '\n the game we exit directly '.upper() + 
            '\nenter (r) to play again or press enter to exit : '.upper())
        def re_play():
            global prompt
            if prompt.lower() != 'r':
                for i in range(1,3):
                    i='.............'  
                print('\ngame exiting...'.upper() + i*30 )

            else:
                
                global exqt_defult
                print('\n\t\t__________----------GOOD-Lucky-------______________'.upper())
                game()

        re_play()

        print("\n\t-------------------------------your total point = ".upper() + '[' + str( point) + ']')

        print('\n\t\t\t\t\texit done'.upper())
        time.sleep(2) 
        print('\n\t\t--------GAME EXIT------------')
        input()
        active=False
    elif namess.upper() == 'Q':
        break
    elif namess.upper() == 'EXIT':
        break
    else:
        print('\nyour name is not thesame  !!!!'.upper())
        active=False
        check=input(retype)
        namess=check
        active=True
