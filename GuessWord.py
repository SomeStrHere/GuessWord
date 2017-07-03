
#GuessWord
#A 'Hangman' like game; where the user is instructed to guess a random word by entering a series of letters.
#Inspiration and guidance came from:
#https://www.youtube.com/watch?v=5aAkDVXxNhk&index=5&list=PLhP5GzqIk6qsYjU_3tod0nqoWGXlq9RvF and
#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
#
#Version 0.1.2
#Versioning: a.b.c
#a = major change, b = smaller change, c = minor changes (bug fixes, etc)
#

#Import libraries
import random
import csv #I'd like to read a list of words from a csv file rather than have them coded in source
import sys #Used to exit the program

def welcomeMenu() :
    """Displays a welcome message to the user and gives a simple menu to start or exit the game."""
    print('\n########################')
    print('#                      #')
    print('#      Guess Word      #')
    print('#                      #')
    print('########################\n')

    print('Please enter (1) Play Game or (2) Exit Game\n')
    menuOption = input()

    if menuOption == '1' :
        playGame()

    elif menuOption == '2' :
        print('\nThank you for playing...\n')
        clearConsole(2)
        sys.exit()
    else :
        clearConsole(0) #clear console without a delay
        welcomeMenu() #reload the menu

def get_word() : #original function to get word from hard coded file

    words = ['Woodstock', 
             'Gary',
             'Sophie']

    #words = readFile()

    return random.choice(words).upper() #returns a random choice from these words

def readFile() : #Read the contents of file words.txt, if file isn't found create it.
    """Read contents of a txtt file."""

    #set permissions for accessing the file
    READ = "r"
    WRITE = "w"
    fileName = "words.txt"

    try :
        with open(fileName, READ) as csvFile :
            listFromFile = csv.reader(csvFile)

        wordList = []
        wordList = listFromFile

    except :
        #Try to read file, if file not found, create file.

        if FileNotFoundError :
            print('File not found...')
            createFile = input('Would you like us to create a new file for you? (Y) ').upper()
            if createFile == "Y" :
                file = open("words.txt", mode = WRITE)
                file.write('Python') #Write the first line of the newly created txt file
                file.close()
                readFile() 
            else :
                welcomeMenu()

    return(wordList) #return wordList derived from the words.txt file

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
    for letter in word : #loop through letters in our word; we can loop through strings in Python
        if letter  in guesses :
            status += letter
        else :
            status += "*"

        if letter == guess :
            matches += 1
    
    if matches > 1 :
        print('Yes! The word contains', matches, '"' + guess + '"' + 's' )
    elif matches == 1 :
        print('Yes! The word contains', matches, '"' + guess + '"')
    else :
        print('Sorry. The word does not contain the letter "', guess + '"')

    return(status)

def playGame() :

    word = get_word()
    guesses = [] #keep track of users guesses in this list
    guessed = False
    print('The word contains', len(word), ' letters.')
    while not guessed:
        text = 'Please enter 1 letter or a {}-letter word. '.format(len(word))
        guess = input(text).upper()
        if guess in guesses :
            print('You already guessed "' + guess + '"')
        elif len(guess) == len(word) :
            guesses.append(guess)
            if guess == word: #if user guessed the correct word, set guessed to true
                guessed = True
            else :
                print('Sorry, that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, guess)
            if result == word :
                guessed = True

            else :
                print(result)

        else :
            print('Invalid entry')

    print('Yes, the word is ', word + '! You got it in ', len(guesses), 'tried.')

def main() :
    welcomeMenu()

#__name__ is a special variable set by Python; if my code runs as a program, __name__ is set by Python
#to __main__ so by testing for this condition code from within this module file can be used by other programs,
#without running the main() function.
if __name__ == "__main__" :
    main()

