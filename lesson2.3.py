math_statement = input("Enter in a math statement: ")

math_terms = math_statement.split(" ")
print(math_terms)
x = float(math_terms[0])
op = math_terms[1]
y = float(math_terms[2])


if op == "*":
    print(x * y)
elif op == "/": 
    print(x / y)
elif op == "+":
    print(x + y)
elif op == ("-"): 
    print(x - y)
else: 
    print('invalid operation')

     
