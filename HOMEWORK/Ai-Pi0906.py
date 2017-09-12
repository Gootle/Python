import time


"""
myDict = {
    'apple': ['a round fruit with red skin', '蘋果'],
    'banana': ['a long fruit with yellow skin', '香蕉'],
    'watermelon': ['a large, round fruit with green skin', '西瓜']
    }


def new_word():
    try:
        word, definition, chinese = input('Enter your new word (word,definition,chinese):\n').split(',')
        if word in myDict:
            print('{} is already in dictionary'.format(word))
        else:
            myDict[word] = [definition, chinese]
            print('word {} added.'.format(word))
    except ValueError:
        print('Please make sure the format is correct.')
    except:
        print('Something happened unexpected!')


"""
def tell_you():
    print('\n')
    print('親愛的阿包\n')
    time.sleep(1)
    print('長尾巴快樂!!\n')
    time.sleep(1)
    print('這是愛屁當媽媽後的第二個生日\n')
    time.sleep(1.5)
    print('看到彤彤一天一天地長大，這一年來也辛苦阿屁了\n')
    time.sleep(2)
    print('今年想換點不一樣的生日禮物給阿屁，因為實在沒梗，暫時只想到弱弱的這樣\n')
    time.sleep(3)
    print('但是豬豬對阿屁的心意不變，希望我們在未來一年可以更好，工作上也有進展\n')
    time.sleep(4)
    print('也希望我們可以互相砥礪 把阿彤顧得更好\n')
    time.sleep(2)
    print('喵 愛屁~~ \n')
    time.sleep(1)
    print('愛你的豬豬    CHU~~\n')
    time.sleep(10)

def help():
    print('親愛的阿包\n, 歡迎來看豬豬第一個Python APP\n')
    print('請按[1] 來看豬豬給阿包的話') 
    print('請按[2] 來看') 
    print('請按[3] 離開程式')
    print('')  

def run():
  
    while True:
        help()
        cmd = input("請問你要選幾?")
        if cmd == '1':
            tell_you()
        elif cmd == '2':
            tell_you()
        elif cmd == '3':
            break
        else:
         print('阿屁\n, 不要選錯 戳戳 \n\n\n\n')   

run()
