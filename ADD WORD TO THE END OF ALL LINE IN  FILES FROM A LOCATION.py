#ADD WORD TO THE END OF ALL LINE IN  FILES FROM A LOCATION.py
#program by : HARFHO


import sys #import module sys
import os  #import module os
get_path= input('INPUT THE FILE PATH(location to the files): ')

base = get_path  # get the file path

what_to_write = input('WHAT DID YOU WHAT TO WRITE AT THE END OF THE FILES: ')

put = '\n' + what_to_write #write to the end of the file

save = os.path.join(base + '/') #get the file location


for file_name in os.listdir(base): #loop through the files in the path.
    file = open(save+file_name,'a+') # open the file as append modes
    file.write(put) #write 

file.close() #close the file
print('successful') 
input()
print('CLOSE')