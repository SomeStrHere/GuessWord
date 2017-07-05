
#GuessWord
#A 'Hangman' like game; where the user is instructed to guess a random word by entering a series of letters.
#Inspiration and guidance came from:
#https://www.youtube.com/watch?v=5aAkDVXxNhk&index=5&list=PLhP5GzqIk6qsYjU_3tod0nqoWGXlq9RvF and
#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
#
#Version 1.1.0
#Versioning: a.b.c
#a = major change, b = smaller change, c = minor changes (bug fixes, etc)
#

#Import libraries
import random
import csv #I'd like to read a list of words from a csv file rather than have them coded in source
import sys #Used to exit the program

#Global variables
userGuessLimit = 8 #set defaul number to 8
def gameLogo() : #Seperated the games console logo so it can be re-used more efficiently
    print('\n########################')
    print('#                      #')
    print('#      Guess Word      #')
    print('#                      #')
    print('########################\n')

def welcomeMenu() :
    """Displays a welcome message to the user and gives a simple menu to start or exit the game."""
    gameLogo() #Displays the games logo; in different function, so it can be efficiently re-used
    #seperatley from the menu components.

    print('Please enter (1) Play Game or (2) Exit Game\n')
    print('Optional: You can alter the default guess limit by pressing (0).\n')
    menuOption = input()

    if menuOption == '1' :
        clearConsole(0)
        gameLogo()
        playGame()

    elif menuOption == '2' :
        print('\nThank you for playing...\n')
        clearConsole(1)
        gameLogo()
        sys.exit()

    elif menuOption == '0' :
        clearConsole(0)
        gameLogo()
        guessLimit()
    else :
        clearConsole(0) #clear console without a delay
        welcomeMenu() #reload the menu

def guessLimit() : #obtain a guess limit from the user and return the limit number
    """Asks the user to select how many attempts they want at guessing the word."""
    
    global userGuessLimit
    default = False

    print("How many attempts would you like to have?\n")
    print('(A) Up to 20 guesses!\n')
    print('(B) Up to 12 guesses!\n')
    print('(C) Only 3 guesses!\n')
    print('...or press any other key for the default.\n') #default is 8
    userChoice = input().upper()

    if userChoice == 'A' :
        userGuessLimit = 20

    elif userChoice == 'B' :
        userGuessLimit = 12

    elif userChoice == 'C' :
        userGuessLimit = 3

    else :
        default = True
        userGuessLimit = userGuessLimit

    clearConsole(0)
    gameLogo()

    if default :
        print('Thank you, the game will start with the default number of guesses')# % userGuessLimit
    else :
        print('Thank you, you have selected %d guesess.\n' % userGuessLimit)

    playGame() #Once the user sets the guess limit, start the game

def getWord() : 
    """Gets list of words from readFile() and returns a random a word out of the list."""

    words = readFile()
 
    return random.choice(words).upper() #picks an element from a sequence

def readFile() : #Read the contents of file words.txt, if file isn't found create it.
    """Read contents of a words.txt file and returns a list of words."""

    #set permissions for accessing the file
    READ = 'r'
    WRITE = 'w'
    #r+ = read and write
    fileName = "words.txt"

    try :
        #used this approach so closing file is handled automatically
        #previousl wasn't able to call dictionary.close() in finally to close the file.
        with open(fileName, READ) as f :
            dictionary = f.readlines() #Reads the entire file

        words = [word.strip() for word in dictionary] #Seperates each word to create a list of words

    except : #Try to read file, if file not found, create file.

        if FileNotFoundError :
            print('File not found...')
            print('Please create file with a list of words, called words.txt in program directory')
            welcomeMenu()
            
    return(words) #return words derived from the words.txt file

def clearConsole(wait) : #function to clear console on Linux or Windows
   """Accepts an integer argument and produces a delay for the number of seconds passed as an argument\
    the program will then attempt to clear the console for Windows, and if that fails will try to clear\
     the console for Linux."""

   import time
   time.sleep(wait) # produces a delay based on the argument given to clearConsole()
    
   import os

   try :
       os.system('cls') #clears console on Windows
   except :
       os.system('clear') #clears console on Linux

def check(word, guesses, guess) :
    status = '' 
    matches = 0
    for letter in word : #loop through letters in 'word'; we can loop through strings in Python
        if letter  in guesses : #if letter is in guesses add that letter to the status string
            status += letter
        else :
            status += "*" #if letter not in guesses add a * to the status string

        if letter == guess :
            matches += 1 #record number of matches for the users guess
    
    if matches > 1 :
        print('\nYes! The word contains', matches, '"' + guess + '"' + 's' )
    elif matches == 1 :
        print('\nYes! The word contains', matches, '"' + guess + '"')
    else :
        print('\nSorry. The word does not contain the letter "', guess + '"')

    return(status)

def playGame() :
    """Determines if a users guess is correct and produces apropriate output."""

    word = getWord()
    guesses = [] #keep track of users guesses in this list    
    guessed = False

    #Added this overall while loop to test leng(guesses) which should give the number of times a user
    #guesses a word against a pre-defined/user set int variable called userGuessLimit.

    print('\nThe word contains', len(word), 'letters.') #tells user how many letters are in the word
    while (not guessed) and (len(guesses) < userGuessLimit):
        text = 'Please enter 1 letter or a {}-letter word. \n\n'.format(len(word))
        guess = input(text).upper()
        if guess in guesses :
            print('\nYou already guessed "' + guess + '"')
        elif len(guess) == len(word) :
            #if users guess is same length as the answer word, assign it to guesses
            guesses.append(guess)
            if guess == word :
                guessed = True
            else :
                print('\nSorry, that is incorrect.')

        elif len(guess) == 1 :
            guesses.append(guess)
            result = check(word, guesses, guess)
            if result == word :
                guessed = True
            else :
                print(result)
        else :
            print('\nInvalid entry')

    #print statement will execute when the user exits the while loop
    if(guessed) :
        print('\nYes, the word is ', word + '! You got it in ', len(guesses), 'tries.')
        print('\nReturning you to the menu...')
        clearConsole(4)
        welcomeMenu()

    else :
        print('\nYou have reached the limit of guesses, please try again...')
        print('Returning you to the menu...')
        clearConsole(4)
        welcomeMenu()

def main() :
    """Calls welcomeMenu() to start the game."""
    welcomeMenu()

#__name__ is a special variable set by Python; if my code runs as a program, __name__ is set by Python
#to __main__ so by testing for this condition code from within this module file can be used by other programs,
#without running the main() function.
if __name__ == "__main__" :
    main()