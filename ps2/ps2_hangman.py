# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def display_word(word, guessed):
	'''
	word (string): randomly chosen word from choose_word function
	guessed (list): list containing all of the guessed letters up to this point
	displays the blanks and letters once a guess has been made
	'''
	for letter in word:
		if letter in guessed:
			print letter,
		else:
			print '_',
	print 
	
def display_guesses(guessed):
	'''
	guessed (list): list containing all of the guessed letters up to this point
	displays all the letters guessed so far
	'''
	print "Guessed Letters: ",
	for letter in sorted(guessed):
		print letter, 
	print
	
def guess_check(word, letter):
	'''
	word (string): randomly chosen word from choose_word function
	letter (char): guessed letter
	checks if the letter is in the word. returns True / False
	displays: Good Guess: or Oops! That letter is not in my word: 
	'''
	if letter in word:
		print 'Good Guess: ',
		return True
	else:
		print 'Oops! That letter is not in my word: ',
		return False
	
def win_check(word, guessed):
	'''
	word (string): randomly chosen word from choose_word function
	guessed (list): list of all the letters that have been guessed
	checks if the list of guessed letters makes up the entire word
	returns True or False 
	'''
	for letter in word:
		if letter not in guessed:
			return False
	return True
	
def hangman():
	print "\nWelcome to the Game of Hangman!"
	
	word = choose_word(wordlist)
	print "I am thinking of a word that is %d letters long." % len(word)
	
	guesses_left = 8
	guessed = list()
	
	while True:
		# Ask for letter and check if it has been guessed already. Check to see if the word has been guessed next.
		# Add to guessed list otherwise and then check if letter is in the word. 
		letter = raw_input("Please guess a letter: ")
		if letter.lower() in guessed:
			print "You have already guessed that letter. Please guess again."
			continue
		elif len(letter) > 1:
			print "You may only enter in one letter. Please guess again."
			continue
		elif not letter.isalpha():
			print "You may only enter letters a - z. Please guess again."
			continue
		else:
			letter = letter.lower()
			guessed.append(letter)
			
		check = guess_check(word, letter)
		display_word(word, guessed)
		
		if win_check(word, guessed):
			print '-----------------------------------'
			print 'Congratulations, you won!'
			break

		if check == False:
			guesses_left -= 1
		
		if guesses_left <= 0:
			print '-----------------------------------'
			print "Oh No! You ran out of guesses!"
			print "My word was: %s" % word		
			break
			
		print '-----------------------------------'
		print 'You have %d guesses left.' % guesses_left
		display_guesses(guessed)
	
# Game Loop
game_over = False
while game_over != True:
	hangman()
	choice = raw_input("Would you like to play again? (Enter [Y]es or [N]o)")
	if choice.lower() == 'n' or choice.lower() == 'no':
		print "Goodbye!"
		game_over = True
	elif choice.lower() != 'y' or choice.lower() == 'yes':
		print "That was not a choice. Oh well, goodbye!"
		game_over = True

	