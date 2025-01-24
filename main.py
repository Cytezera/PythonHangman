import random 
def initializeGame():
    words = [ 'apple' , 'tree' , 'ice', 'fire' , 'toast' , 'airport' , 'paper' , 'paper' , 'mouse' , 'orange']
    guesses = 10 
    word = random.choice(words)
    seen = set()
    return word 

def checkWordInGame(word, getInput, hiddenWord):
    for index, char in enumerate(word):
        if char == getInput:
            hiddenWord[index] = char 
    return hiddenWord 

def getUserInput(seen, word , hiddenWord): 
    while True:  
        getInput = str(input("Please select a character: " ).lower())
        if len(getInput) != 1: 
            print ("Character more than 1, please try again" ) 
            continue
        if getInput not in seen:
            seen.add(getInput)
            checkWordInGame(word, getInput , hiddenWord)
            break; 
        print ("You have already selected this word" ) 
    return hiddenWord 

def displayGame(guesses, hiddenWord):
    print (f"Number of guesses left : {guesses}")   
    print ("Current Word: ") 
    print ("".join(hiddenWord))
def menu():
    guesses = 10 
    word = initializeGame() 
    seen = set()
    hiddenWord = ["_"] * len(word)
    print("Hello there !" ) 
    print("Please guess your word" ) 
    while guesses > 0: 
        displayGame(guesses, hiddenWord)
        hiddenWord = getUserInput(seen,word, hiddenWord)
        if "".join(hiddenWord) == word:
            print ("Congratualtions !")
            print (f"You got it in {10-guesses} tries") 
            break;
    
    print (f"The word wss {word}") 
menu()

