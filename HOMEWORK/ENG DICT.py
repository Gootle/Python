MyDict = {
    'apple': ['red fruit','蘋果'],
    'orange': ['orange fruit','橘子'],
    'banana': ['yallow fruit', '香蕉']
    }

def list_all_words():
    print('Your word list\n')
    for key, value in MyDict.items():
        print('{} ({})\n {}'.format(key, value[1], value[0]))
        
        
        
              
def test_yourself():
    quit_the_test = False
    point = 0
    incorrect_word_list = []
    for key, value in MyDict.items():
        while True:
            answer = input('\n Whicj word matches the defintion? or [c]hinese, [p]ass, [q]uit\n{}'.format(value[0]))
            if answer == 'c':
                print('{}'.format(value[1]))

            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
                break
            elif answer =='q':
                quit_the_test = True
                break
            elif answer ==key:
                print('Good Job!')
                point += 1
                break
            else:
                print('It\'s not correct')
                incorrect_word_list.append(key)
          
        if quit_the_test == True:
             break
            
    print('\n Score{}/{}'.format(point, len(MyDict)))
    print('Incorrect word list:')
    for key in incorrect_word_list:
        value = MyDict[key]
        print('{} [{}]\n {}'.format(key, value[1], value[0]))
        
def run():
    while True:
        cmd = input("""\n Welcome to Dict!
(1) Test yourself
(2) list all word
(3) exit\n""")
        
        if cmd == '1':
            test_yourself()
        elif cmd == '2':
            list_all_words()
        elif cmd == '3':
            break
    
run()                    
