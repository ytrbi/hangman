import random
from arts import title_art

print(title_art)

words = ['luxury', 'quiz', 'icebox', 'juicy', 'voodoo', 'cycle', 'equip', 'pajama', 'oxygen', 'pixel', 'galaxy', 'funny', 'zigzag', 'staff', 'scratch', 'jazz', 'mouse', 'jungle', 'notebook', 'frug', 'pizza', 'rocket', 'calendar', 'algebra', 'chocolate', 'koala', 'unicorn', 'father']
secret_word = random.choice(words)

print(secret_word)

blanks = ['_'] * len(secret_word)
tempts = 0 

print(f'The word length is {len(secret_word)}')
print(f'You have to guess the word: {" ".join(blanks)}')


while tempts <= 8 :
    user_guess = input('Make a guess: ').lower()
    tempts += 1

    for i in range(len(secret_word)):
        if secret_word[i] == user_guess:
            blanks[i] = user_guess
    if '_' in blanks:
        print(f'You have {8 - tempts} attempts left')
    elif  tempts == 8:
        print('You lost! The word was: ' + secret_word)
    else:
        print('You guessed the word!')
        break
    print(f'Updated word: {" ".join(blanks)}')
