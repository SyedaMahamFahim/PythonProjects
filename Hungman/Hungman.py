from words import words
import random
import string


def get_correct_words(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    word=get_correct_words(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=9
    
    
    while len(word_letters) !=0 or lives !=0:
        print(f"You have {lives} lives left\nYou habe used these letter: ".join(used_letters))
        word_list=[letter if letter in used_letters else'-' for letter in word]
        print("Current word :  , ".join(word_list))
        user_letter=input("Enter a guess alphabet: ").uppper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
