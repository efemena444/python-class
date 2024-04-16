import random
footballTeams = ["man utd","arsenal","chelsea","real madrid","inter miami","psg","juventus"]
chosenWord = random.choice(footballTeams)
wordlength = len(chosenWord)
print(f"chosen word is {chosenWord}")
display = []

for _ in range(wordlength):
    display +=  "_"
#print(display)
endOfGame = False
while  not endOfGame  :   
    guess = input("guess a word:").lower()
    

    for position in range(wordlength):
        letter = chosenWord[position]
    if letter == guess:
        display[position] = letter
        
    print(display)
   
    if "_"  not in display:
        endOfGame = True
        print("you win")
    

