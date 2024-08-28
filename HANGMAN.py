import random
from  collections import Counter

someWords = ("apple banana mango strawberry orange grape black blue "
             "white yellow car train bus watermelon mercedes bmw audi koenigsegg papaya peach ")

someWords = someWords.split(' ')
# randomly choose a secret word from our 'someWords' list.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: there is no hint try it alone :) ')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0 ) and flag == 0 : #flag is updated when the word is correcrtly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a leter!')
                continue

            #Validation of the guess
            if not guess.isalpha():
                print('Enter only a Letter')
                continue
            elif len(guess) > 1:
                print('Enter only a Single Letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # if letter is guesses correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess # the guesses letter is added as many times as it occurs

            # print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char,end=' ')
                    correct += 1
                # if user haS guessed all the letters
                # once the correct word is guesses fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You Won!')
                    break # To break out of the for loop
                    break # To break out of the while loop
                else:
                    print('_', end=' ')
        #if user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You Lost! Try Again...')
            print('The word was {}'.format(word))
    except keyboardInterrupt:
        print()
        print('Bye! Try Again.')
        exit()



