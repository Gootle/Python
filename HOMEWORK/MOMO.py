file = open('todolist.txt', 'r') #讀取
file.readline() #讀第一行


file.seek(0) #回第0行

for line in file:
    print(line)  #print預設會換行

    # print (line, end='') 不會換行


file.close() #關閉檔案
# 如果with open 用完就關閉

