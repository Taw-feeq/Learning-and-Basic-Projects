mydict={"name": "Tawfeeq", "age": "20", "status": "Student", "city": "Chennai"}
print(mydict)

mydict1=dict(name="Tawfeeq", age=20, status= "Student", city= "Chennai")
print(mydict1)

value= mydict["name"]                               #cant use a key that's not in the dictionary 
print(value)    
print(mydict1["city"])

mydict["email"]="tawfeeq@gmail.com"                 #adds a new key value pair to the dictionary
print(mydict)

mydict["email"]="tawfeeqmd123@gmail.com"            #overwrites the value 
print(mydict)

del mydict1["name"]                                 #delete specified key value pair
mydict1.pop("age")                                  #delete specific key value pair
mydict1.popitem()                                   #delete last key value pair
print(mydict1)                                      
del mydict1                                         #deletes the enire dictionary

print(mydict.keys())                                #returns all the keys in it
print(mydict.values())                              #returns all the values in it
print(mydict.items())                               #returns all the key value pairs as pairs 

newdict={"name": "Muhammad", "age": 21, "hobby": "Movies", 1: 100}

mydict.update(newdict)                              #rewrites the existing values and adds the non existing values
print(mydict)

mytuple=(25,75)
mydict2={mytuple: 100}                              #tuple can also be used as a key, but not a list
print(mydict2)

