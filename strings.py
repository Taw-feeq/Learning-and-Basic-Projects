from timeit import default_timer as timer

name="I'm Tawfeeq"
name='I\'m Tawfeeq'
print(name)

my_str="Hello World"
print(my_str)
print(my_str[1])
print(my_str[-1])

print(my_str[2:])
print(my_str[:8])

print(my_str[::1])
print(my_str[::2])
print(my_str[::-1])

print(my_str.upper())
print(my_str.lower())

print(my_str.count('l'))
print(my_str.find('l'))
print(my_str.find('lo'))

print(my_str.startswith('Hell'))
print(my_str.endswith('rld'))

print(my_str.replace('world', 'Chennai'))
print(my_str.replace('World', 'Chennai'))

my_str="Hello World, Myself Muhammad"
my_list= my_str.split(',')
print(my_list)
my_list= my_str.split()
print(my_list)

new_string=""
new_string=''.join(my_list)
print(new_string)
new_string=' '.join(my_list)
print(new_string)

l=['x']*250000
#print(l)

#bad
start=timer()
new_l=""
for i in l:
    new_l += i
#print(new_l)
stop=timer()
print(stop-start)

#good
start=timer()
new_str=''.join(l)
#print(new_str)
stop=timer()
print(stop-start)

str1="str"
var1=3.14159
var2=18

string="The variable values are %s, %d and %.3f" %(str1,var2,var1)
print(string)

string="The variable values are {}, {} and {:.4f}".format(str1,var2,var1)
print(string)

string=f"The variable values are {str1}, {var2} and {var1:.2f}"
print(string)
