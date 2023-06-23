import requests
import webcraweler2
from datetime import date
import datetime

# ==============================
#      Notify設定
# ==============================

def notify(msg, token):
    url = "https://notify-api.line.me/api/notify"         # Notify網址 
    headers = {"Authorization": "Bearer " + token}        # HTTPS表頭
    payload = {"message": message}                        # HTTPS內容
    requests.post(url, headers=headers, params=payload)   # 提出POST請求
    

# 發送訊息
token = '''你的token'''     # 你的token
usd_currency = webcraweler2.show_usd_currency()
today = date.today()
yesterday = today + datetime.timedelta(days = -1)         # 取得昨日日期

message = "\n%s的美金\n買入為%s，賣出為%s" %(yesterday, usd_currency[0], usd_currency[1])
notify(message, token)

