import os
candidates={}
highest_bidder=""
highest_bid=0
is_their_any_bidder="Yes"


while is_their_any_bidder!="No":
    name=input("Enter your name: ")
    bid=int(input("Enter your bid: "))
    candidates[name]=bid
    is_their_any_bidder=input("Are there more bidders ? Type 'Yes' if any else 'No'.")
    if is_their_any_bidder=="Yes":
        os.system('cls')


for i in candidates:
    if candidates[i]>highest_bid:
        highest_bid=candidates[i]
        highest_bidder=i
print(f"The highest bidder is {highest_bidder} who bidded ${highest_bid}.")