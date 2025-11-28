import json

# 用來儲存使用者輸入的資料
data = []

# 設定輸入的條件
while True:
    # 讓使用者輸入名稱和數量
    name = input("請輸入貨幣名稱（例如：比特幣 (BTC)）：")
    quantity = input(f"請輸入{name}的數量：")
    
    # 嘗試將數量轉換為整數，並處理錯誤
    try:
        quantity = int(quantity)
    except ValueError:
        print("數量必須是數字，請重新輸入。")
        continue
    
    # 將輸入的資料加入列表
    data.append({"name": name, "quantity": quantity})
    
    # 是否繼續輸入
    more = input("是否要繼續輸入？（y/n）：")
    if more.lower() != 'y':
        break

# 將資料寫入 data.json 檔案
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("data.json 已經成功生成！")
