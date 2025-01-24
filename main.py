import random 
def initializeGame():
    words = [ 'apple' , 'tree' , 'ice', 'fire' , 'toast' , 'airport' , 'paper' , 'paper' , 'mouse' , 'orange']
    guesses = 10 
    word = random.choice(words)
    seen = set()
    return word 

def checkWordInGame(word, getInput, hiddenWord,guesses):
    for index, char in enumerate(word):
        if char == getInput:
            hiddenWord[index] = char 
            return guesses
    guesses -= 1 
    return guesses 
def getUserInput(seen, word , hiddenWord, guesses): 
    while True:  
        getInput = str(input("Please select a character: " ).lower())
        if len(getInput) != 1: 
            print ("Character more than 1, please try again" ) 
            continue
        if getInput not in seen:
            seen.add(getInput)
            guesses = checkWordInGame(word, getInput , hiddenWord, guesses)
            break; 
        print ("You have already selected this word" ) 
    return hiddenWord , guesses

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
        hiddenWord, guesses  = getUserInput(seen,word, hiddenWord,guesses)
        if "".join(hiddenWord) == word:
            print ("Congratualtions !")
            print (f"You got it in {10-guesses} tries") 
            break;
    
    print (f"The word wss {word}") 
menu()

