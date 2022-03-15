#Use open the file and read the content (By default MODE is always 'r')

f = open("sample.txt", "r")
# print(f.read())                   # it will read whole file text
#print(f.read(20))                  # it will read only 20 character from this file
print(f.readline())                 # it will read only FIRST line from this file
print(f.readline())                 # it will read only SECOND line from this file
print(f.readline())                 # it will read only THIRD line from this file
f.close()


#NOTE:- readline() function can be use MORE THAN ONE time, each function will read the new line. 