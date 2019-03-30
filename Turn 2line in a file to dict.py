print('THE PROGRAM TAKE TWO LINE IN A FILE AND TURN IT INTO DICTIONARY THEN SAVE IT.')

filename=input('filename: ')#a variable Holding filename
def file(filename='C://new.txt'):      
    locate = filename #storing the file name in a  local variable locate
    file=open(filename,'r+') #open the file as read and write 
    edit = [] # store the line in the list as list
    for line in file:
        edit.append(line.replace('\n','').strip())

    creat = open(filename.replace('.txt','.list'),'w+') #recreate file but with extension list
    creat.write(str(edit))#store the list created in the filename
    creat.close() #close the file 

def Newfile():
    Name=input('Save place in full: ')   #Hold the save place the user specify
    load = open(filename.replace('.txt','.list')) #open the filename with the extention list 
    fill = load.read() #Read it into memory
    fill_list = eval(fill) #Evaluate the file in it original data type()  list
    d = dict(zip(*[iter(fill_list)]*2)) #iterate through the list with 2 item and trun it into dict
    
    reload=open(Name.replace('.txt','.dict')+'.dictionary','w+')  #create file with the user input in Name variable 
    reload.write(str(d)); #save the created dict
    reload.close() #close the file
    
file(filename)
Newfile()
print('DONE')
input()