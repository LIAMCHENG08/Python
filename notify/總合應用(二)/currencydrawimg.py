import pandas as pd
import matplotlib.pyplot as plt

def draw():
    data = pd.read_csv("ExchangeRate_USD.csv")

    clean_data = pd.DataFrame({"日期":[data.iloc[i,0] for i in range(len(data)-1,-1,-1)],
                               "本行買入":[data.iloc[i,3] for i in range(len(data)-1,-1,-1)],
                               "本行賣出":[data.iloc[i,13] for i in range(len(data)-1,-1,-1)]})
    
    # 設定畫布
    plt.figure(figsize=(16,6))
    
    # 設定中文
    plt.rcParams["font.family"] = "Microsoft JhengHei"
    plt.rcParams["font.size"] = 12
    plt.rcParams["axes.unicode_minus"] = False
    
    # 畫折線圖
    plt.plot(clean_data.index, clean_data["本行買入"],color="#0E12F9", label="本行買入")
    plt.plot(clean_data.index, clean_data["本行賣出"],color="#FA001B", label="本行賣出")
    
    # 調整x軸標籤
    label = [(str(clean_data.iloc[i,0])[4:]) for i in range(0,len(clean_data),4)]
    plt.xticks(range(0,len(clean_data),4), labels=label, rotation=45)
    
    # 設定x軸與y軸標題
    plt.xlabel("日期")
    plt.ylabel("匯\n率", rotation=0)
    
    # 設定圖例及網格
    plt.legend(title="現金匯率", ncol=2, loc=9)
    plt.grid(axis="y")
    
    # 儲存圖表
    plt.savefig("bankcurrency.jpg")
    
    plt.show()
    