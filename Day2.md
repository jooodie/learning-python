# 砍斷重練 - python

## Grammar notes, Day 2 - for loop

```
for i in range(5):
    print("第", i, "次Hello")
```
### 🗣️Note: range(5) ➔ 從 0 到 4，不包含5本身！Python 的範圍是「前包後不包」。

range()的規則：
```
用法	                         意義	                                   範例
range(n)	                   從0到n-1	range(5)                      → 0,1,2,3,4
range(start, end)	           從start到end-1	range(2,6)              → 2,3,4,5
range(start, end, step)	     從start到end-1，每次加step	range(1,10,2) → 1,3,5,7,9
```

| 用法         | 意義 | 範例             |
|--------------|------|------------------|
| `[]range(n)`         | `從0到n-1	range(5)`  | range(5) → 0,1,2,3,4           |
| `range(start, end)`       | `從start到end-1`  |range(2,6) → 2,3,4,5    |
| 🌟`range(start, end, step)`     | `從start到end-1，每次加step	range`  |range(1,10,2) → 1,3,5,7,9       |



### for迴圈搭配list
```
python

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

```

output
```

apple
banana
cherry

```

### Q1 不用自己定義 i = 0嗎？ 
👉是的！(in python) 因為 for 迴圈的 range() 幫你自動處理了。
### Q2 沒有定義 fruit 是什麼，它怎麼知道要印list裡的東西？ 
👉 因為 for loop 在讀 list 時，是自動幫你把每個元素「一個一個取出來」，交給你設定的變數（這裡是 fruit）使用

👉 fruit的名稱可以換成任何你想要的（只要自己記得是什麼就可以）

---

## Small Task印出九九乘法表
<img width="413" alt="截圖 2025-04-21 上午9 28 54" src="https://github.com/user-attachments/assets/efd10d02-e914-41b4-8912-65d571197c2f" />
