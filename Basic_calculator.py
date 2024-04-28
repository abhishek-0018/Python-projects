import os
def calc(a,o,b):
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    else:
        return a/b
    
a=int(input("Enter first number: "))
o=input("Enter operation (+,-,*,/)")
b=int(input("Enter second number: "))
r=calc(a,o,b)
print(f"Output of {a} {o} {b} is: {r}")
cont=int(input(f"Press 1 if you want to continue with {r}, 2 if you want to continue with mew number and 3 to abbort"))
while cont != 3:
    os.system("cls")
    if cont==1:
        a=r
    else:
        a=int(input("Enter first number: "))
    o=input("Enter operation (+,-,*,/)")
    b=int(input("Enter second number: "))
    r=calc(a,o,b)
    print(f"Output of {a} {o} {b} is: {r}")
    cont=int(input(f"Press 1 if you want to continue with {r}, 2 if you want to continue with mew number and 3 to abbort"))