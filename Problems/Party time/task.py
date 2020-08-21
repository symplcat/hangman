import random
from string import ascii_lowercase

print(' '.join('hangman'.upper()) + '\n')
answer = list(random.choice(["python", 'java', 'kotlin', 'javascript']))
hint = list("-" * len(answer))
lives = 8
prev_guesses = []
while lives > 0 and '-' in hint:
    print(''.join(hint))
    guess = input("Input a letter: ")
    if not 0 < len(guess) < 2:
        print("You should input a single letter")
    elif guess not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
    elif guess not in prev_guesses:
        if guess in answer:
            prev_guesses += guess
            for i in range(len(answer)):
                if answer[i] == guess:
                    if guess not in prev_guesses:
                        hint[i] = guess
                    else:
                        print("You already typed this letter")
                        break
        else:
            if guess not in prev_guesses:
                prev_guesses += guess
                print('No such letter in the word')
                lives -= 1
    else:
        print("You already typed this letter")

if lives == 0:
    print("You are hanged!")
else:
    print("You survived!")
