import random
a=["Rock","Paper","Scissor"]
i=int(1)
while i!=0:
    c=int(input("What is your choice? 0 for rock, 1 for paper and 2 for scissor\n"))
    if c<0 or c>2:
      print("Invalid choice. Please select from 0, 1 and 2\n")
      continue
    r=random.randint(0,2)
    if c==0:
       if r==0:
        print(f"You choose {a[c]} and computer also choose {a[r]}. So, it's a draw\n")
       elif r==1:
         print(f"You choose {a[c]} and computer choose {a[r]}. So, you lost\n")
       else:
         print(f"You choose {a[c]} and computer choose {a[r]}. So, you won\n")
    elif c==1:
       if r==0:
        print(f"You choose {a[c]} and computer choose {a[r]}. So, you won\n")
       elif r==1:
         print(f"You choose {a[c]} and computer also choose {a[r]}. So, it's a draw\n")
       else:
         print(f"You choose {a[c]} and computer choose {a[r]}. So, you lost\n")
    else:
       if r==0:
        print(f"You choose {a[c]} and computer choose {a[r]}. So, you lost\n")
       elif r==1:
         print(f"You choose {a[c]} and computer choose {a[r]}. So, you won\n")
       else:
         print(f"You choose {a[c]} and computer also choose {a[r]}. So, it's a draw\n")
    i=int(input("Press 1 if you want to continue, otherwise 0\n"))