#Concatination
#Len
#Upper
#Lower
#Strip
#Split
#Replace
#Substring

text = "This is my first python script"

length = len(text)
print("Length of the text:" , length)

str1 = "Hello"
str2 = "World"
concat = str1 + " " + str2
print(concat)

upper = text.upper()
print("Upper :" , upper)

lower = text.lower()
print("Lower :" , lower)


split = text.split()
print("Lets split" , split)

replace_text = ("first" , "second")
print(replace_text)

Text = "Python is awesome"
substring = "is"
if substring in Text:
    print(substring , "Found in Text")