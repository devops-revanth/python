print("Hello World!")

#Concatination

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)


#Len
text = "Python is awesome! brother"
length = len(text)

print("The lenght of the string is:", length)


#Upper
#Lower
text = "Python is fun!"

uppercase = text.upper()
lowercase = text.lower()

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)


#Replace
text = "Python is fun!"
next_text = text.replace("Python", "Ansible")
print("Modified text:", next_text)


#Split
text = "Python is awesome"
words = text.split()

print("Words:", words)



#Strip
text = "   Some spaced around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)


#Substring
text = "Python is awesome!"
substring = "is"
if substring in text:
    print(substring, "found in the text")



# Fload Variables
num1 = 5.0
num2 = 2.5

#Basic Arithmetic
result1 = num1 + num2
print("Addition: " , result1)

result2 = num1 - num2
print("Subtraction : " , result2)

result3 = num1 * num2
print("Multiplication :" , result3)

result4 = num1 / num2
print("Division :" , result4)

# Rounding
result5 = round(3.1432564664 , 2) # Rounds to 2 decimal places
print("Rounded : " , result5)


#withoutfunctions
num1 = 10
num2 = 5

addition = num1 + num2
print(addition)

sub = num1 - num2
print(sub)

multiplication = num1 * num2
print(multiplication)

division = num1 / num2
print(division)


#withfunctions
a = 10
b = 5

def addition():
    add = a + b
    print(add)

def subtraction():
    sub = a-b
    print(sub)

def multiplication():
    mul= a*b
    print(mul)

addition()
subtraction()
multiplication()


#input functions
def addition(num1 , num2):
    add = num1 + num2
    return add
def subtraction(num1 , num2):
    sub = num1 - num2
    return sub
def multiplication(num1 , num2):
    mul = num1 * num2
    return mul

print(addition(10 , 5))

print(subtraction(10 , 5))

print(multiplication(2 , 4))



print("Hello World")


str1 = "High file"
str2 = "Count detected"
str = "Python is awesome"

#Concatination
result1 = str1 + str2 # Concatination
print("This result is for Concatination : " , result1)




# num1 = 10
# num2 = 5
# 
# addition=num1 + num2
# print(addition)
# 
# sub=num1-num2
# print(sub)
# 
# mul=num1 * num2
# print(mul)
# 
# 
# def addition():
    # add = num1 + num2
    # print(add)
# 
# def subtraction():
    # sub = num1 - num2
    # print(sub)
# def multiplication():
    # mul = num1 * num2
    # print(mul)
# 
# addition()
# subtraction()
# multiplication()


def addition(num1 , num2):
    add = num1 + num2
    return add
def subtraction(num1 , num2):
    sub = num1 - num2
    return sub
def multiplication(num1 , num2):
    mul = num1 * num2
    return mul

print(addition(10 , 5))
print(subtraction(10,5))
print(multiplication(10,5))




## Day 1 -  Print Hello World

print("Hello World!")

## Day2 - DataTypes - String , Integer

## String - Concat , Len , Upper , Lower , Split , Strip , replace , Sustring

str1 = "Hello"
str2 = "World"
str = "Python is Awesome"
text = "      Hello everyone , Lets do well for our    job        "


##Concat 

result1 = str1 + str2
print( "Concatination result of ", str1 , "and" , str2 ,  "is : " , result1)
print( f"Concatination result of {str1} and {str2} is : {result1}")


##Len

length = len(str)

print(f"length of {str} is : {length}")

#Upper

Upper = str.upper()

print(f"Lets convery our {str} to upper and result is {Upper}")

#Lower 

Lower = str.lower()

print(f"Now lets convery {str} to lower and the result is {Lower}")


# Strip

strip_text = text.strip()

print(f"Now removing spaces before and after contence and the result is {strip_text}")

#replace

replace_str = str.replace("Awesome" , "Fun")

print(f"Replace contence in {str} with Fun and the result is {replace_str}")


##Split

split_result1 = replace_str.split()
split_result2 = str.split()
split_result3 = strip_text.split()

## We are splitting 3 contents

print(f"First result in split with {replace_str} as input and the result is : {split_result1}")
print(f"Second result in split with {str} as input and the result is : {split_result2}")
print(f"Third result in split with {strip_text} as input and the result is : {split_result3}" )


## Substring

substring = "is"

if substring in str:
    print(f"We are verifying '{substring}' is in '{str}' or not -> if you get the result then '{substring}' is in '{str}'")


## Interget and float

num1 = 10.0
num2 = 5.0

add = num1 + num2
print(f"Addition of {num1} and {num2} is : {add}")

sub = num1 - num2
print(f"Subtraction of {num1} and {num2} is : {sub}")


mul = num1 * num2
print(f"Multiplication of {num1} and {num2} is : {mul}")

div = num1 / num2
print(f"Division of {num1} and {num2} is : {div}")

fdiv = num1 // num2
print(f"Floor division of {num1} and {num2} is : {fdiv}")

exp = num1 ** num2
print(f"Explonention of {num1} and {num2} is : {exp}")


mod = num1 % num2
print(f"Modulas of {num1} and {num2} is : {mod}")


num3 = -5
num4 = 453.33323232332323

## Round
result_round = round(num4 , 2)
print(f"{result_round}")

## ABS

result_abs = abs(num3)
print(f"{result_abs}")




## Without Functions

num1 = 10
num2 = 5

add = num1 + num2
print(f"Addition of {num1} and {num2} is : {add}")

sub = num1 - num2
print(f"Subtraction of {num1} and {num2} is : {sub}")


mul = num1 * num2
print(f"Multiplication of {num1} and {num2} is : {mul}")


## With Functions


def addition():
    add = num1 + num2
    print(add)

def subtraction():
    sub = num1 - num2
    print(sub)

def multiplication():
    mul = num1 * num2
    print(mul)


addition()
multiplication()
subtraction()

## Input output Return

def addition(num3 , num4):
    add = num3 + num4
    return add

def subtraction(num3 , num4):
    sub = num3 - num4
    return sub

def multiplication(num3 , num4):
    mul = num3 * num4
    return mul


print(addition(4,6))
print(multiplication(2,4))
print(subtraction(10,5))



