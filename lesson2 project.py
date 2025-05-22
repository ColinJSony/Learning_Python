def add(a+b)
 return a + b
def sub(a-b)
 return a - b
def div(a/b)
 return a / b
def mul(a*b)
 return a * b

math_statement = input("Enter in a math statement: ")

math_terms = math_statement.split(" ")
print(math_terms)
x = float(math_terms[0])
op = math_terms[1]
y = float(math_terms[2])


if op == "*":
    print(mul(x,y))
elif op == "/": 
    print(div(x,y))
elif op == "+":
    print(add(x,y))
elif op == ("-"): 
    print(sub(x,y))
else: 
    print('invalid operation')

     
