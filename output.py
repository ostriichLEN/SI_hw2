import json
import matplotlib.pyplot as plt
import platform  # for 判斷作業系統

def create_pie_chart(json_file):
    try:
        # 讀取 JSON 檔案
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 提取資料
        labels = [item['name'] for item in data]
        sizes = [item['quantity'] for item in data]

        # 跨平台字體支援
        current_os = platform.system()
        
        if current_os == 'Windows':
            # Windows 繁體中文標準字型：微軟正黑體
            print("偵測到 Windows 系統，設定字型為微軟正黑體...")
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei']
        elif current_os == 'Darwin':
            # Darwin 即為 macOS
            print("偵測到 macOS 系統，設定字型為 Arial Unicode MS...")
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC']
        elif current_os == 'Linux':
            # Linux 常見中文字型
            print("偵測到 Linux 系統，設定通用中文字型...")
            plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Droid Sans Fallback']
        else:
            print(f"未知系統 ({current_os})，嘗試使用預設字型...")
            
        # 解決負號顯示為方塊的問題
        plt.rcParams['axes.unicode_minus'] = False

        # 繪製圓餅圖
        fig, ax = plt.subplots(figsize=(8, 6))
        
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
        
        ax.axis('equal') 
        plt.title("資產分佈圓餅圖", fontsize=16)

        plt.show()

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{json_file}'")
    except KeyError:
        print("錯誤 : JSON 格式不符，請確認包含 'name' 和 'quantity' 欄位")
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")

if __name__ == "__main__":
    create_pie_chart('data.json')