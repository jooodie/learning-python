### Day5 小專案

請加油！

---
### 我的迷你小助理
Function: 
1. To-do list
2. remember my firends birthday
3. serching dictionary

Process:
1. 新增待辦事項（儲存到 List）
2. 查詢朋友生日（從 Dictionary 查)
3. 查詢單字翻譯（從 Dictionary 查）
4. 離開程式

Fram structure:
<img width="363" alt="截圖 2025-04-28 下午12 26 26" src="https://github.com/user-attachments/assets/19df328a-fae6-4618-8c91-aa4133588361" />

```
tasks = []
    
birthday = {
    "Julie" : "MAy 29th",
    "Alex" : "April 5th",
    "Alibek" : "Nov 19th"
}

dictionary = {
    "apple" : "蘋果",
    "banana" : "香蕉",
    "avacado" : "酪梨"
}

def add_task():
    todo = input("Enter your To-do item: ")
    tasks.append(todo)
    print(todo, "added in To-do list")


def Serching_birthday():
    friend = input("enter a friend's name:")
    if friend in birthday:
        print(friend, "'s birthday is", birthday[friend])
    else:
        print("找不到這個朋友的生日")
    
    
def dictionary_data():
    word = input("enter a word:")
    if word in dictionary:
        print(word, dictionary[word])
    else:
        print("This dictionary doesn't have this word")



while True:
    print("---My personal assistant---")
    print("1. Add new To-do things")
    print("2. Serching friend's birthday")
    print("3. Serching the dictionary")
    print("4. break ")
    
    choice = input("plz enter(1-4):")

    if choice == "1":
        add_task()
    elif choice == "2":
        Serching_birthday()
    elif choice == "3":
        dictionary_data()
    elif choice == "4":
        print("Seeya")
        break
    else:
        print("error")


```
##### ✨先定義變數（這裡是我的集合）再定義Function，最後才是主程式
##### ✨記得 縮!排!  pyton才知道被包進loop funtion裡面



