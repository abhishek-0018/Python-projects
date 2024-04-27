letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input("Please enter a string that you want to be encoded.\n")
n=int(input("Please enter the shift position that you want.\n"))
code_again="yes"
while code_again!="no":
    encode_or_decode=input("Type encode for encoding and decode for decoding.\n")
    if encode_or_decode=="encode":
        encoded_string=""
        for i in s:
            if i in letters:
                encoded_string+=letters[(ord(i)-97+n)%26]
            else:
                encoded_string+=i
        print(f"Your encoded string would be {encoded_string}.")
    else:
        decoded_string=""
        for i in encoded_string:
            if i in letters:
                decoded_string+=letters[(ord(i)-97-n)%26]
            else:
                decoded_string+=i
        print(f"Your decoded string would be {decoded_string}.")
    code_again=input("Type yes if you want to continue, else no.\n")