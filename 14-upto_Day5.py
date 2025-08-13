### Day1 Scripts

print("Hello World!")


### Day2 Scripts

### String in-built functions
## Concat
## Len
## Upper
## Lower
## Split
## Substring
## replace
## Strip

text = "Python is awesome"

str1 = "Hello"
str2 = "Raj , Name tho sunavo"

Concat = str1 + str2
print("Concatincation output" , Concat)


length = len(text)

print("Length output " ,length)

Upper = text.upper()
Lower = text.lower()

print("Upper output" , Upper)
print("Lower output" , Lower)

Split = text.split()
print("Split output" , Split)

replace = text.replace("awesome" , "fun")
print("Replace out put : " , replace)

raju = "         Raju is a good boy          "
strip = raju.strip()

print("Stripping output  " , strip)

substring = "is"
if substring in text:
    print("Substring output : " , substring , "Found in text")


#################################################

### Float and integer

a = 10
b = 3
c=-5

add = a+b
sub = a-b
mul = a*b
div = a/b



print(add)
print(sub)
print(mul)
print(div)

r= round(div , 2)
print(r)


mod = a%b
divi=a//b
abs=abs(c)

print(mod)
print(divi)
print(abs)


######################################################

##Day3
my_variable=42
print(my_variable)

## Local variable
def my_function():
    x=10
    print(x)
my_function()

## Global variable
y=20
def another_function():
    print(y)
another_function()
print(y)

####################################################

