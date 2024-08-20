import random
import arts

print(arts.title_art)

words = ['luxury', 'quiz', 'icebox', 'juicy', 'voodoo', 'cycle', 'equip', 'pajama', 
         'oxygen', 'pixel', 'galaxy', 'funny', 'zigzag', 'staff', 'scratch', 'jazz', 
         'mouse', 'jungle', 'notebook', 'frug', 'pizza', 'rocket', 'calendar', 
         'algebra', 'chocolate', 'koala', 'unicorn', 'father']

secret_word = random.choice(words)
blanks = ['_'] * len(secret_word)
incorrect_attempts = 0
max_attempts = 6

print(arts.hangman_stages[0])
print(f'The word length is {len(secret_word)}')
print(f'You have to guess the word: {" ".join(blanks)}')

while incorrect_attempts < max_attempts:
    user_guess = input('Make a guess: ').lower()

    if user_guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == user_guess:
                blanks[i] = user_guess
    else:
        incorrect_attempts += 1

    arts.display_hangman(incorrect_attempts)

    if '_' not in blanks:
        print('You guessed the word!')
        break

    print(f'Updated word: {" ".join(blanks)}')
    print(f'You have {max_attempts - incorrect_attempts} attempts left')

if incorrect_attempts == max_attempts:
    print('You lost! The word was: ' + secret_word)
