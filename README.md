# 軟體工程導論作業二
### 組員
- 1122926 張佑杰
- 1122930 闕帝軒

## 專案結構

- `Input.py`: 用於接收使用者輸入的腳本。
- `output.py`: 用於讀取並顯示儲存資料的腳本。
- `data.json`: 儲存使用者輸入資料的 JSON 檔案。
- `README.md`: 本說明檔案。

## 如何使用

請依照以下步驟執行本專案：

### 1. 執行 `Input.py` 來儲存您的資料

在終端機中執行 `Input.py`。腳本會提示輸入名稱與數量。

```bash
python Input.py
```

輸入完成後，資料將會被輸出成 `data.json` 檔案。

### 2. 執行 `output.py` 來讀取`data.json`並繪製圓餅圖

執行 `output.py` 來讀取 `data.json` 中的資料，並將其顯示在終端機上。

```bash
python output.py
```

腳本會根據`data.json`繪製出圓餅圖。

## 檔案說明

- **`Input.py`**
  - 提示使用者輸入名稱與數量。
  - 將輸入的資料打包成一個 Python 字典。
  - 將字典轉換為 JSON 格式並寫入 `data.json` 檔案。

- **`output.py`**
  - 讀取 `data.json` 檔案。
  - 解析 JSON 資料。
  - 根據 `data.json` 繪製出圓餅圖。

- **`data.json`**
  - 一個用來在兩個腳本之間傳遞資料的暫存檔案。
  - 格式如下：
    ```json
    {
        "name": "2330", // 名稱(以股票代碼為例，2330:台積電)
        "quantity": 500 // 數量
    }
    ```
