## Welcome to our DS workshop brought to you by DataScience circle @CATReloaded

## let's start with python variables

## var_name = value

x=10 ##int
y=3.5 ##floating point
z="c" ##
a="Hello!"

## to get the data type of the variable 

print(type(x))

## operators 
#addition , subtraction , mul,division / , division // , %, ** exp, - 

print(5/2)
print(5//2)

## printing 
#python adds spaces in printing
print("Hello, World!")
print ("Hello,","World!")

#built in functions like...
print(min(10,20,30))
print(max(10,20,30))
print(abs(-100)) #absolute value
#type casting
print(int(y))
print(float(x))

# help function gets info about any built in function in case
# you forgot what it does
help(print)
## control statements
num1=20
num2=30
if num1>num2:
    print("num1 bigger")
elif (num1<num2):
    if (z==1):

        print("num1 smaller")
else:
    print("equal")        
#Scope of variables and 4 spaces instead of braces

#definig your own functions and Docstrings to use help with them

## With no return "void"
def decide_smallbig_num(t,u,v):
    """This function takes 3 paramaters and print the largest
    and the smallest one of them
    >>>decide_smallbig_num(50,60,1200)
    the smallest=50
    the largest=1200
    """
    print ("the smallest=",min(t,u,v))
    print("the largest=",max(t,u,v))
print(help(decide_smallbig_num))

# with return 

def math_op (c,op_char,d):
    if op_char=='+':
        return c+d
    elif op_char=='-':
        return c-d
    elif op_char =='*':
        return c*d 
    elif op_char== '/':
        return c/d
    else:
        return None    
#print(math_op(5,'//',10)) 
# loops
for i in range(5):
    print(i)
name="CATReloaded"
for ch in name:
    print(ch)   
c=0
while c<11:
    print(c)
    c+=1  
## lists, python version of arrays the difference that they're can be dynamic like vectors or static like arrays
#they can have elements of different data types pr pf the same type

ls = [20,30,40,50,60]
print(len(ls))

print(ls[0])
print(ls[-1])
print (ls[1:])
print(ls[1:4])
# mutable
ls.append(70)
ls[0:2]=[0,1]
# other list methods pop, clear,count,sort,reverse,copy
##list comprehension
#a concise way to create lists
squares=[r**2 for r in range(10)]

##dicts, key / index data structure consists of key/value pairs and 
# keys must be unique
d1= dict()
#or
d2={}

d3=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#looping over dicts
for k,v in d3.items():
    print(k,v)

##lambda functions/ anonymous functions : without names
# any number of ars but only 1 expression

def squared(number):
    return number **2

lm= lambda f : f**2
print(lm(5))
print(squared(5))

#ls3=list(map(lambda r:r**2 ,range(10)))


