# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    mistake_found = False
    word_check = ''.join(set(str(secret_word)))
    #print(word_check)
    for i in range(0,len(word_check)):
        char = word_check[i]
        #print('Checking: ' + char)

        for j in letters_guessed:
            if (str(char) == j):
                #print 'match', char
                break
            else:
                #print 'Not a match'
                if j == letters_guessed[len(letters_guessed)-1]:
                    mistake_found = True
                    break
                else:
                    continue
                #mistake_found = True

        if i == len(word_check)-1 and mistake_found == False:
            #print('You have guessed the word correctly')
            return True
        elif mistake_found == True:
            #print('You havent guessed the word correctly')
            return False
        else:
            continue

#print is_word_guessed('morten','netom')
# print is_word_guessed('apple',['a','e','l','p'])
# print ['a','e','l','p']


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    user_word = ''
    for i in secret_word:

        #print(i)
        for j in letters_guessed:
            if j == i:
                user_word = user_word+j
                #print('match', user_word)
                break
            else:
                if j == letters_guessed[len(letters_guessed)-1]:
                    user_word = user_word+'_'
                else:
                    continue
    return user_word


#print(get_guessed_word('apple',['g','n','l','e']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list(string.ascii_lowercase)

    for char in letters_guessed:
        alphabet.remove(char)
    return ''.join(alphabet)
#print(get_available_letters(['a','b','m']))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman! \n')
    print('I am thinking of a word that has ' + str(len(secret_word)), 'letters.')

    warnings_left = 3
    guesses_left = 6
    letters_guessed = []

    while guesses_left > 0:

        check = False

        print('\n---------------')
        print('You have ' + str(guesses_left) + ' guesses left')
        print('Available letters: ' + str(get_available_letters(letters_guessed)))

        #Get input and check if its correct format
        while not check:
            guess = input("Please guess a letter: ").lower()
            if guess.isalpha() and guess not in letters_guessed: #Correct input from user
                check = True
            elif warnings_left>0:
                print('Please make sure to enter only one letter you havent prevoisly entered')
                warnings_left -= 1
                print('Warnings left before you lose a guess: ', warnings_left)

                if warnings_left == 0:
                    print('No warnings left, you\'ve lost a guess')
                    guesses_left -= 1

            elif warnings_left == 0:
                print('No warnings left, you\'ve lost a guess')
                guesses_left -= 1

        #Add guess to list
        letters_guessed.append(guess)
        print('Secret word so far: ', get_guessed_word(secret_word, letters_guessed))

        #Check if user has guessed the secret word
        if is_word_guessed(secret_word,letters_guessed):
            print('You have correctly guessed the word!')
            print('Score: ', (guesses_left*len(''.join(set(secret_word)))))
            break

        print('---------------')
        guesses_left -= 1
    if guesses_left == 0:
        print('You have run out of guesses, the secret word was', secret_word)







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":


    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
