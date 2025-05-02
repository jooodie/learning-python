# Day6 
LeetCode 類 Easy 題解＋解題流程練習

---
🔍 今日重點技能

學會拆解題目邏輯（流程思維）

熟悉 Python 中 list / string / if-else 的使用

開始養成：先講流程 → 再寫程式 的習慣

---
### 👾 題目：判斷是否為回文（Palindrome）
```
🧠 Step 1：想流程（這是Day6最重要的練習）

我們可以問自己：
輸入是什麼？ ➔ 一個字串
要處理什麼？ ➔ 檢查反轉過來是不是一樣
輸出是什麼？ ➔ 是就回傳 True，不是就回傳 False

🧪 Step 2：用人話寫一遍邏輯
輸入字串 → 把它反轉 → 比較跟原本是否一樣 → 一樣就回傳 True，不一樣就回傳 False

🧩 Step 3：開始寫程式（先從最簡單版本）
```

<img width="313" alt="截圖 2025-05-02 下午1 02 41" src="https://github.com/user-attachments/assets/0c42e86b-9e7e-4621-845a-e5b88df30975" />

```
* [::-1] 是 Python 字串的一個「切片（slice）語法」：
  word[::1]	正常順序（從頭到尾）
  word[::-1] 反轉順序（從尾到頭）
* return ➜ 是「回傳一個值」給外面用
* word == word[::-1] ➜ 這個表達式的結果是一個布林值（Boolean），會是 True 或 False

💡 在 Python 裡：
x = 5 > 3
print(x)       # 印出 True
print(5 > 10)  # 印出 False
✅ 比較運算（==, !=, >, <...）自動產生 True / False
你不需要自己去定義 True / False，Python 語言本身就已經提供這兩個布林常數了！

So, 用 == 去做對比 ➔ 得到 True/Fasle
再用 return 把這個結果回傳出去
```

### Q&A
```
❓那為什麼不一定要用 if 判斷呢？
  因為當我只需要知道結果（True / False），這樣就可以了（當作工具函數使用）;
  但如果我今天需要根據 True / False 做不同的事，那就要搭配 if 用（作流程控制邏輯用）


❓為什麼我們需要判斷「是否為回文」？什麼情況會用到？
  「回文」不是重點，而是你是否能發現資料的「對稱性」、並利用它做邏輯判斷。
```


### Challenge：忽略大小寫與空格，是否為回文
"A man a plan a canal Panama"

流程邏輯
1. 全部轉小寫、空白不寫入
2. 判斷是否為回文
<img width="313" alt="截圖 2025-05-02 下午1 02 41" src="https://github.com/user-attachments/assets/994c4d97-5ab9-4dee-8c47-b649ccc11f69" />


### 總結
```
✨ Judy超重要的收穫：

.replace("a", "b") 是「全部取代」
.lower() 是轉成小寫
[::-1] 是字串反轉技巧
== 是布林值比較 → 回傳 True/False
```





