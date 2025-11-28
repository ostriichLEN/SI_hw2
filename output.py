import json
import matplotlib.pyplot as plt

def create_pie_chart(json_file):
    try:
        # 1. 讀取 JSON 檔案
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 2. 提取資料
        # 假設 JSON 是一個列表，包含 name 和 quantity
        labels = [item['name'] for item in data]
        sizes = [item['quantity'] for item in data]

        # 3. 設定中文字型 (專為 MacOS 優化)
        # 如果不設定這行，圖表上的中文會變成方框
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
        plt.rcParams['axes.unicode_minus'] = False

        # 4. 繪製圓餅圖
        fig, ax = plt.subplots(figsize=(8, 6)) # 設定圖片大小
        
        # autopct='%1.1f%%' 代表顯示小數點後一位的百分比
        # startangle=90 代表從 12 點鐘方向開始畫
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
        
        ax.axis('equal')  # 確保圓餅圖是正圓形
        plt.title("資產分佈圓餅圖", fontsize=16)

        # 5. 顯示圖表
        print("圖表生成中...")
        plt.show()

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{json_file}'")
    except KeyError:
        print("錯誤：JSON 格式不符，請確認包含 'name' 和 'quantity' 欄位")
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")

if __name__ == "__main__":
    create_pie_chart('data.json')