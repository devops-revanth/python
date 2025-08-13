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


