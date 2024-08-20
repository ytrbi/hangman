<<<<<<< HEAD
=======
# Title art
>>>>>>> v1.0.1 | Added ASCII art for Hangman stages
title_art = """
.---.  .---.    ____    ,---.   .--.  .-_'''-.   ,---.    ,---.   ____    ,---.   .--. 
|   |  |_ _|  .'  __ `. |    \  |  | '_( )_   \  |    \  /    | .'  __ `. |    \  |  | 
|   |  ( ' ) /   '  \  \|  ,  \ |  ||(_ o _)|  ' |  ,  \/  ,  |/   '  \  \|  ,  \ |  | 
|   '-(_{;}_)|___|  /  ||  |\_ \|  |. (_,_)/___| |  |\_   /|  ||___|  /  ||  |\_ \|  | 
|      (_,_)    _.-`   ||  _( )_\  ||  |  .-----.|  _( )_/ |  |   _.-`   ||  _( )_\  | 
| _ _--.   | .'   _    || (_ o _)  |'  \  '-   .'| (_ o _) |  |.'   _    || (_ o _)  | 
|( ' ) |   | |  _( )_  ||  (_,_)\  | \  `-'`   | |  (_,_)  |  ||  _( )_  ||  (_,_)\  | 
(_{;}_)|   | \ (_ o _) /|  |    |  |  \        / |  |      |  |\ (_ o _) /|  |    |  | 
'(_,_) '---'  '.(_,_).' '--'    '--'   `'-...-'  '--'      '--' '.(_,_).' '--'    '--' 
"""

<<<<<<< HEAD

# print(title_art)
=======
# Gallows art by incorrect guesses
hangman_stages = {
    0: """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    1: """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    2: """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    3: """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    4: """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    5: """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    6: """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
}

# Function to display the hangman art based on incorrect guesses
def display_hangman(incorrect_guesses):
    print(title_art)
    print(hangman_stages.get(incorrect_guesses, hangman_stages[6]))  # Defaults to complete figure if out of range


>>>>>>> v1.0.1 | Added ASCII art for Hangman stages
