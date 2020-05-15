# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
      if char in lettersGuessed:
        flag = True
      else:
        flag = False
        break
    return flag



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ""
    for char in secretWord:
        if char in lettersGuessed:
            guessed = guessed + char
        else:
            guessed = guessed + "_"
    return guessed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters = string.ascii_lowercase

    for letter in lettersGuessed:
        allLetters = allLetters.replace(letter, "")
    return allLetters
    


def hangman(secretWord):
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

# Driver Block
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

