#simple div
str_input = input("a: ")

a = int(str_input)
#print(type(a))

operation = input("+ / * - ^ ")

str_input2 = input("b: ")

b = int(str_input2)
#print(type(b))

if operation == '/':
    result = a / b
elif operation == '+':
   result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '^':
    result = a ** b
else:
    result = "unknown"
    
#print(type(result))
print("Result: " + str(result))