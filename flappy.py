alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x = alphabet.index("z")
print(x)
userinput = input("enter your message:")
shift = int(input("enter the shift number:"))
def encrypt(plain_text , shift_amount):
    encryptedText = ""
    for _ in plain_text:
        if _ in alphabet:
            position = alphabet.index(_)
            #print(position)
            newPosition = shift_amount + position
            new_ = alphabet[newPosition]
            encryptedText += new_
    print(encryptedText)
encrypt(plain_text=userinput,shift_amount=shift)    
    
    
              
            