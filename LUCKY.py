import random
Word = ['A', 'B', 'C', 'D', 'E']
LuckyWord = random.choice(Word)

for i in range(3):
    print('There is {} Words'.format(Word))
    guess = input('Guess your lucky Word:')
    if guess != LuckyWord:
        print ('{} is not your lucky word'.format(guess))
        Word.remove(guess)
    else: break

if guess == LuckyWord:
    print(' {} is your lucky word'.format(LuckyWord))
    
else:
    print('Acturally {} is your Lucky Word'.format(LuckyWord))

    
        
