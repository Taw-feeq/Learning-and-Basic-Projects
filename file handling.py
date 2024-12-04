f=open("fruits.txt")            #read mode      and     to open the file specify the extension 
print(f)                        #returns the memory address of the file
print(f.read())                 #reads the content of the file
f.close()                       #must close the opened file 

f=open("fruits.txt", "w")       # write mode 
f.write("mango\n")              #erases all the previous data and replaces it with the given value
f.close()

f=open("fruits.txt", "r+")      # r+ means it can also do read as well and write operation 
print(f.read())                 
f.close()

f=open("fruits.txt", "a")       #append mode, appends the value without erasing the previously stored values
f.write("apple\n")              #\n is used to append the value in the next line or else
f.write("orange\n")             #it will append it in the single line w/o space
f.write("banana\n")
f.write("pineapple\n")
f.close()

f=open("fruits.txt")            
print(f.read())

