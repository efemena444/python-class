import random
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Numbers = ["0","1","2","3","4","5","6","7","8","9"]
Special_characters = ["!","@","#","$","%","^","&","*","()","_","+"]
print("welcome to the password generator")
userLetter = int(input("how many lettetrs would you like in your password:"))
userNumber = int(input("how many numbers would you like in your password:")) 
userchar = int(input("how many special characters would you like in your password:"))
password = ""
for char in range (1,userLetter + 1):
    password += random.choice(Letters)
    print(password)
for char in range (1,userNumber + 1):
    password += random.choice(Numbers)
    print(password)    
for char in range (1, userchar +1):
    password += random.choice(Special_characters)
    print(password)    