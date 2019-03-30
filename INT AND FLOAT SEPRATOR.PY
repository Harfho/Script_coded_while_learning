#author Harfho
float=float(input('type a number : '.upper()))#convert the  number user enter into a float

string=str(float)#convert it ot string

int_=int(float)#convert it to integer

dotfind=string.find('.')#find the index of . in string 

dot_place=(string[dotfind:])#assign the index of the . and slice it to the end

print('\noriginal'.upper(),float)

print('\nint part='.upper(),int_)

print('\ndot part='.upper()+ str(dot_place))

input()
