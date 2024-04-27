import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','=','_','+','`','~','{','}','[',']','|','?']
print("Welcome to pasword generator!")
nl=int(input("How many letters would you like in your password?\n"))
ns=int(input("How many symbols would you like in your password?\n"))
nn=int(input("How many numbers would you like in your password?\n"))
s=""
a=[]
for i in range(1,nl+1):
    r=random.randint(0,51)
    s+=letters[r]
    a.append(letters[r])
for i in range(1,ns+1):
    r=random.randint(0,21)
    s+=symbols[r]
    a.append(symbols[r])
for i in range(1,nn+1):
    r=random.randint(0,9)
    s+=numbers[r]
    a.append(numbers[r])
print(f"The simple password would be {s}.\n")
password=""
for i in range(1,nl+ns+nn+1):
    k=random.randint(0,len(a)-1)
    password+=a[k]
    a.remove(a[k])
print(f"The strong password would be {password}.\n")