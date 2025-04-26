# Day3 

今天有一個壞消息，我發現我day2的內容沒有commit到😱...
anyway學習還是得繼續 keep on it!

今天要學的是：
## List 串列


```
fruits = ["apple", "banana", "cherry"]
```
[] 表示這是一個 List
內容可以是任何東西（字串、數字、布林值、甚至別的 List）


> 修改 List 的內容
```
fruits[1] = "grape"
print(fruits)  # ["apple", "grape", "cherry"]
```
✅ List 是 可變的（mutable），所以可以自由改內容。



### List 常用操作 
| 操作方式                     | 範例程式碼                     | 說明                     |
|------------------------------|--------------------------------|--------------------------|
| 建立 List                    | `fruits = ["apple", "banana"]` | 建立一個字串串列          |
| 取得元素（依照索引）         | `fruits[0]`                   | 取得第一個元素 `"apple"`  |
| 修改元素                     | `fruits[1] = "grape"`         | 把 `"banana"` 改成 `"grape"` |
| 加入元素到最後              | 🌟`fruits.append("orange")`     | 將 `"orange"` 加到最後   |
| 移除特定元素（依值）         | `fruits.remove("apple")`      | 移除 `"apple"` 這個元素   |
| 計算元素數量                 | `len(fruits)`                 | 回傳元素總數              |
| 排序（小到大）               | `fruits.sort()`               | 依字母順序排序            |
| 倒序排列                     | `fruits.reverse()`            | 把順序反轉                |
| 清空整個 List               | `fruits.clear()`              | 移除所有元素，變成空陣列   |
| 檢查是否存在某值             | `"apple" in fruits`           | 回傳 True 或 False       |
| 加總 List 數字總和（int/float）| `sum(scores)`                 | 計算整個數字 List 的總和  |
| 計算平均值（數值型 List）     | `sum(scores)/len(scores)`     | 計算
---

## 【for 迴圈搭配 list】

> 插播一則breaking news！
我的day2回來了！我那天把整個網頁縮小，今天用的是全新的網頁，意外點到另一個完整網頁看到我的new file裡面是day2的內容，第一反應是開心，第二反應是啊我剛剛打的day3咧...
結果都還在😭太好了！果然努力不會白費！（咦？
（接續for loop:))

# for loop combined list 可以用來「逐一處理」list 裡的內容！
<img width="413" alt="截圖 2025-04-24 下午6 22 39" src="https://github.com/user-attachments/assets/f6178f59-d45a-4fff-a103-e92fcbb5de50" />


## 【List 裡可以存數字，也可以計算】
```
scores = [80, 95, 70]
print("總分：", sum(scores))
🌟print("平均：", sum(scores) / len(scores))
```

---


## pratice 1：動態加東西進去
```
list_of = []
list_of.append("sun")
list_of.append("beach")
list_of.append("bekini")

print("summer 3 essential: ", list_of)
```

### ourput: 
```
summer 3 essential:  ['sun', 'beach', 'bikini']
```
- Cuz python list will print whole data strcture（Python 幫你印出「內部長相」）
- But, If U want to outcome looks like: summer 3 essential:  sun, beach, bikini.
- We should use '.join'

```
print("summer 3 essential: " + ", ".join(list_of) + ".")

or

print("🌞夏日三寶有：" + " / ".join(list_of) + " ✨")
```

## pratice 2, let user add some in the list
<img width="413" alt="截圖 2025-04-26 上午9 10 08" src="https://github.com/user-attachments/assets/5aa4031a-b6c4-44c5-8236-a7b19c0f6027" />

> 以後學到 while迴圈，可以做到讓使用者想輸入幾個就輸入幾個（自由輸入）






















