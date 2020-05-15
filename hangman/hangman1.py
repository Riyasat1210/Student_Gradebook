from ps3_hangman import *
secretWord = 'hangman'

# secretWord
# lettersGuessed
# mistakesMade
# availableLetters

def hangman_sep(secretWord):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')

    guessesLeft = 8
    lettersGuessed = []

    while(guessesLeft > 0):
        ## Welcome Statements
        print('-----------')
        print('You have '+ str(guessesLeft) + ' guesses left')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        
        # inputs
        guess = input('Please guess a letter: ')
        
        ## Check if Already Inpur
        if guess in lettersGuessed:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + guessedWord)
            ifFlag = False
        else:
            ifFlag = True

        lettersGuessed += guess.lower()
        
        ## New Entry
        guessedWord = getGuessedWord(secretWord, lettersGuessed)

        if guess in secretWord and ifFlag:
            print('Good guess: ' + guessedWord )
            
            if isWordGuessed(secretWord, lettersGuessed):
                print('------------')
                return print('Congratulations, you won!')
                
        elif ifFlag:
            print('Oops! That letter is not in my word: ' + guessedWord)
                #getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1  
    
    print('------------')
    return print('Sorry, you ran out of guesses. The word was ' + secretWord)




hangman_sep('tact')
        
        ## Debuggin ##
        # value = isWordGuessed(secretWord, lettersGuessed)
        # print('Letters Guessed: ' + str(lettersGuessed))
        # print('Flag Value: ' + str(value))
        ######
