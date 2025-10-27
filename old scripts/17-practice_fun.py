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
