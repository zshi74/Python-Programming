import random

""" let the first letter to be the max """
def most_repeated_letters(word_1):
  max_letter = word_1[0]
  max = word_1.count(word_1[0])
  for c in word_1:
    if word_1.count(c) > max:
       max = word_1.count(c)
  return max

  """ count the number of vowels and consonants """
def has_equal_letters(word_2):
  vowel = ("a","e","i","o","u")
  vowels = 0
  consonants = 0
  for char in word_2:
    if char in vowel:
      vowels += 1
    if not (char in vowel):
      consonants += 1
  if vowels == consonants:
    return True
  else:
    return False

  """ firstly evaluate the first letter and the last letter """
def is_palindrome(word_3):
	left_char = 0
	right_char = len(word_3) - 1
	while right_char >= left_char:
		if not word_3[left_char] == word_3[right_char]:
			return False
		left_char = left_char + 1
		right_char = right_char - 1
	return True

""" use the idea from midterm1 """
def total_points(word):
  x = len(word)
  if most_repeated_letters(word) >= 3:
    x = (1/3)*x
  elif most_repeated_letters(word) == 2:
    x = x * 2
  if has_equal_letters(word) == True:
    x = x * 2
  if is_palindrome(word) == True:
    x = x * 5
  return x

  """ count how many y in the two words """
def is_trick_round(p1_word, p2_word):
  n1 = p1_word.count('y')
  n2 = p2_word.count('y')
  if (n1+n2) % 2 == 0:
    return False
  else:
    return True


def get_computer_play():
    """
    Chooses a random word from this list of ridiculous English words and returns it
    """
    return random.choice(['Ailurophile', 'Assemblage', 'Becoming', 'Beleaguer',
                          'Brood', 'Bucolic', 'Bungalow', 'Chatoyant', 'Comely',
                          'Conflate', 'Cynosure', 'Dalliance', 'Demesne', 'Demure',
                          'Denouement', 'Desuetude', 'Desultory', 'Diaphanous',
                          'Dissemble', 'Dulcet', 'Ebullience', 'Effervescent',
                          'Efflorescence', 'Elision', 'Elixir', 'Eloquence',
                          'Embrocation', 'Emollient', 'Ephemeral', 'Epiphany',
                          'Erstwhile', 'Ethereal', 'Evanescent', 'Evocative',
                          'Fetching', 'Felicity', 'Forbearance', 'Fugacious',
                          'Furtive', 'Gambol', 'Glamour', 'Gossamer', 'Halcyon',
                          'Harbinger', 'Imbrication', 'Imbroglio', 'Imbue',
                          'Incipient', 'Ineffable', 'Ingenue', 'Inglenook',
                          'Insouciance', 'Inure', 'Kayak', 'Labyrinthine',
                          'Lagniappe', 'Lagoon', 'Languor', 'Lassitude', 'Leisure',
                          'Lilt', 'Lissome', 'Lithe', 'Love', 'Mellifluous',
                          'Moiety', 'Mondegreen', 'Murmurous', 'Nemesis', 'Numbered',
                          'Offing', 'Onomatopoeia', 'Opulent', 'Palimpsest',
                          'Panacea', 'Panoply', 'Pastiche', 'Penumbra', 'Petrichor',
                          'Plethora', 'Propinquity', 'Pyrrhic', 'Python',
                          'Quintessential', 'Ratatouille', 'Ravel', 'Redolent',
                          'Riparian', 'Ripple', 'Scintilla', 'Sempiternal', 'Seraglio',
                          'Serendipity', 'Summery', 'Sumptuous', 'Surreptitious',
                          'Susquehanna', 'Susurrous', 'Talisman', 'Tintinnabulation',
                          'Umbrella', 'Untoward', 'Vestigial', 'Wafture',
                          'Wherewithal', 'Woebegone'])

def play_game():
    """
    Runs the word game, user vs computer, using your functions.
    Will not work until you have them implemented correctly!
    """
    cutoff = 30       # CHANGE THIS IF YOU WANT A LONGER GAME!
    user_total = 0
    comp_total = 0

    print "First to", cutoff, "points wins!"
    print

    while user_total < cutoff and comp_total < cutoff:

        # get the user and computer words, convert to lower case
        user_word = raw_input("Your play:").lower()
        comp_word = get_computer_play().lower()
        print "Computer played", comp_word

        # calculate user and computer scores
        user_score = total_points(user_word)
        print "User score:", user_score
        comp_score = total_points(comp_word)
        print "Computer score:", comp_score

        # check whether this was a trick round, and score appropriately
        # round winner's score is added, round loser's score is subtracted
        is_trick = is_trick_round(user_word, comp_word)
        if is_trick:
            print "TRICK ROUND!"
        if (is_trick and user_score < comp_score) or (not is_trick and user_score > comp_score):
            print "You win!"
            user_total += user_score
            comp_total -= comp_score
        elif (is_trick and user_score > comp_score) or (not is_trick and user_score < comp_score):
            print "You lose!"
            user_total -= user_score
            comp_total += comp_score
        else:
            print "You tie!"

        # display current score totals
        print "Current scores:"
        print "\tYou:", user_total
        print "\tComputer:", comp_total
        print

    # display overall winner
    print "Game over:",
    if comp_total > user_total:
        print "Computer wins!"
    else:
        print "You win!"

if __name__ == "__main__":
    play_game()
