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

#####EXPERMIENT:
#-Use sets indstead and related methods to do the task


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
    if len(my_word) == len(other_word): #Only check words of same length

        #Get unique characters from my word
        unique_my_word = ''.join(set(my_word)).replace('_','')
        unique_other_word = ''.join(set(other_word))
        #Get position for the characters from my word
        unique_pos = []
        for char in unique_my_word:
            unique_pos.append([[pos for pos, c in enumerate(my_word) if char == c],char])
        print(unique_pos, '\n')

        guide_pos = []
        for char in unique_other_word:
            guide_pos.append([[pos for pos, c in enumerate(other_word) if char == c],char])

        print(guide_pos)

        for i in range(len(unique_pos)):
            pointer =unique_pos[i][1]

            for j in range(len(guide_pos)):
                if pointer == guide_pos[j][1]:
                    #print("Found you")
                    #Check position arrays match over
                    if unique_pos[i][0] == guide_pos[j][0]:
                        #print('Match')
                        continue
                    else:
                        #print('Not a match')
                        return False
                else: #Means that the words dont match over i.e there some character different
                    if pointer in other_word:
                        continue
                    else:
                        return False
        return True



        #Check other_word if the positions line up
        # for i in range(len(unique_chars)):
        #     char_positions = pos[i][0] #
        #
        #     for j in char_positions:
        #         if my_word[j] == '_':
        #             continue
        #         elif my_word[j] == other_word[j]:
        #             print('Match')
        #         elif my_word[j] != other_word[j]:
        #             print('Not a match for: ', other_word[j])
        #             return False
        # return True


    else:
        return False


#print(match_with_gaps('m_vt','move'))
#print(match_with_gaps('te_t','tact'))
print(match_with_gaps('t__t','tact'))
