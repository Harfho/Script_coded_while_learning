import sys #import module sys
import os,time  #import module os time


def creat():
    global file,new_file
    print('\n---------------')
    print('\t'+dir +' checked')
    print('\n---------------')
    while True:
        try:
            new_file = open(save+folder+dir,'w+')
            break
        except UnicodeDecodeError:
            print('-----------')
            print('Sorry File type can not be open'.upper())
            print('-----------')
            continue
        
    file_name = dir 
    file = open(save+file_name,'r+') # open the file as read modes
    while True:
        try:
            for lines in file:
                line = lines
                if what_to_remove in line:
                        removed=line.replace(what_to_remove,'')
                        new_file.write(removed)
                        time.sleep(1)
                        print(what_to_remove + ' was removed')
                elif what_to_remove not in line:
                    new_file.write(line)
                else:
                    print('NO('+what_to_remove+')Found in '+dir)
            break
        except UnicodeDecodeError:
            print('-----------')
            print('Sorry File type can not be open'.upper())
            print('-----------')
            break



while True:
    get_path= input('INPUT THE FILE PATH(location to the files)\nHelp(GO TO THE FILES FOLDER COPY THE PATH AT THE TOP AND PASTE IT HERE): ')
    try:
        base = get_path  # get the file path
        save = os.path.join(base + '\\') #get the file location
        list_dir = os.listdir(base)
        break
    except OSError:
        print('\n---------------------------------------------------')
        print(str('Path ('+ save +') specify can not been found\n'.upper()))
        print('-----------------------------------------------------')
        time.sleep(2)
        continue
        
time.sleep(2) 
print('\n----------path found----------'.upper())    
print(str(r'files found in '+save + '\nare--------------------').title())

for items in (list_dir):
    time.sleep(0.2)
    print('\t\t'+items)
print('-------------------------')
print('PROGRAMMED BY HARFHO')
print('-------------------------')
time.sleep(1)

what_to_remove = input('\nWHAT DID YOU WANT TO REMOVE FROM THE FILES: '.upper())
print('----------')
print('Note---(ALL ('+what_to_remove+') found in the file will be removed')
print('\nif no('+what_to_remove+')found file will not be affected'.upper())
print('----------')
space = ['','  ','   ','    ','     ']
while True:
    confirmed = input('press enter to continue or type exit to cancel: '.upper())
    if confirmed in space:
        break
    elif confirmed.lower() == 'exit':
        print('Programmed Closed')
        time.sleep(0.6)
        sys.exit()
    else:
        continue


while True:
    folder_make = input('save to which Folder: '.upper())
    if folder_make=='':
        print("Can't save folder with space".upper())
        continue
    try:
        os.makedirs(save+folder_make)
    except FileExistsError:
        print('-------file ('.upper()+folder_make +' Exist )-------'.upper())
        rewrite = input('press Enter to save the file in '+folder_make + ' or enter new name: '.upper())
        skip =['',' ','  ','    ']
        if rewrite in skip:
            folder_make=folder_make
            break
        if rewrite:
            folder_make = rewrite
            os.makedirs(save+folder_make)
            break
    else:break

folder = folder_make + '/'
print('SAVING FILES IN '+folder_make.upper())
for dir in list_dir:
    if os.path.isdir(save+dir):
        continue
    else:
        creat()
    
    file.close()
                
                
    new_file.close()
    
    


time.sleep(1)
print('......................\n\tCongrat file edited was successfully Done.......'.upper())
print('you can re_open this program again if you what to remove another text'.upper())
input('Presss Enter to exit'.upper())