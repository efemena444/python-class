import random 
secret_number = random.randint(1,100)
print("welcome to guessing game")
for guess_count in range(0,5):
   guess =int(input("guess the random number:"))
   
   if guess == secret_number:
    print("congratulations")
    break
   elif guess  < secret_number:
       print("too low")
   elif guess > secret_number:
       print("TOO HIGH")
    
    

    
    

