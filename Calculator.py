#simple div
str_input = input("Hello it's calculator ")
str_input = input("Please write X")
x = int(str_input)
#print(type(x))
operation = input ("What operation do you need:")
str_input2 = input("Please write Y: ")
y = int(str_input2)
#print(type(y))
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '/':
   if y!= 0:
      result = x / y  
    else 
     print("You can't /0")     
elif operation == '*': 
 result = x * y
elif operation == '^':
    result = x**y
else:
    result = "unknown"

#result = x / y
#print(type(result))
print("Result: " + str(result))