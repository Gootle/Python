import random

colors = ['red', 'blue', 'green', 'purple', 'yellow']
luckyColor = random.choice(colors)

for i in range(3):
    print('There are {} colors'.format(colors))
    guess = input('Guess your lucky color: ')
    if guess != luckyColor:
        print('Seems like {} is not your lucky color:('.format(guess))
        colors.remove(guess)
    else:
        break

if guess == luckyColor:
    print('Great! {} is your lucky color!'.format(luckyColor))
else:
    print('Actually, {} is your lucky color!'.format(luckyColor))



        
    
    
