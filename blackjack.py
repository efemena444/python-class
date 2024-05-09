import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_cards=random.choice(cards)
    return(random_cards)
usercard =  []
computercard=[]
game_over = False
for i in range(2):
        new_card = deal_card
        usercard.append(new_card)
        computercard.append(new_card)
def calculatescore(cards):
    if sum == 21 and len(cards)==2: 
      return 0
    if 11 in cards and sum(cards)>21 :   
      calculatescore.remove(11)
      calculatescore.append(1)
      return sum(cards)
while not game_over:    
 userscore = calculatescore(usercard)
computerscore = calculatescore(computercard)
print("show userscore:")
print("show computerscore:")
if computercard == 0 or usercard == 0 or userscore > 21:
    game_over = True
else:
   drawcard =int(input("draw another card?:"  "y = drawcard , n = gameover"))
   if drawcard =="y":
     usercard.append(deal_card)
   else:
     game_over = True
     while computerscore == 0:  computerscore < 17
computercard.append(deal_card)
computerscore = calculatescore(computercard)
print(f"card at hand, usercard:finalscore ,userscore:")
print(f"card at hand ,computercard:finalscore , computerscore:")

def compare(userscore,computerscore):
   if computerscore == userscore:
     return 0
   if computercard == 0:
     print("user loses") 
     if usercard == 0:
       print("user wins")
       if userscore > 21:
         print("user loses")
         if computerscore > 21:
           print("computer loses")
           


     

    
    
    


 
      
     
    



     ;