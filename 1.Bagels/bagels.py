'''This simple game was made using a tutorial in "The Big Book of Small Python projects
by Al Swiegart. In this game you guess a number based on clues'''

import random

NUM_DIGITS= 3 #set this to higher numbers to make this game harder and harder
MAX_GUESSES = 10 #More or less guesses for the user, self explanatory

def main(): #I've discovered that 'main' is usually autoatically executed by a program whenever it starts up, i dont know if python does that but we'll find out
    print('''Bagels, a deductive logic game made by Al Swiegart
    
    I am thinking of a {}-digit number with no repeated digits. Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct AND in the right position.
    Bagels          No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS)) #Oh cool, so by putting .format(string) outside the print statement, i can make it automatically slap that string inside the {}

    while True: #Main game loop.
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print(' You have {} guesses to get it right.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looping till a valid gues is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #They got it right, so break out of the loop
            if numGuesses > MAX_GUESSES:
                print("Sorry chief, you rant out of guesses")
                print("The right answer was{}".format(secretNum))

        #Ask player if they want to play again
        print("Wann play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers) #woah holy crap. so he achieved this by making a list of all digits, randomizing it, and then picking the first X number of digits from the list. I was wondering how he would prevent the program from selecting duplicate numbers.

    # Get the first NUM_DIGITS in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    #This returns a string with the pico, fermi, bagels clues.
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct clue is in an incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' #No correct digits at all
    else:
        #sort the clues into alphabetical order so the order doesnt give it away
        clues.sort()
        #make a single string from the list of string clues.
        return ' '.join(clues)


#If the program is run instead of being imported, run the game:
if __name__ == '__main__':
    main()

