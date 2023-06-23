import requests
from datetime import date
import datetime
import currencydrawimg
import webcraweler2

# ==============================
#      Notify設定
# ==============================

currencydrawimg.draw()
usd_currency = webcraweler2.show_usd_currency()

# 取得昨日日期
today = date.today()
yesterday = today + datetime.timedelta(days = -1)

def notify(msg, token, image):
    url = "https://notify-api.line.me/api/notify"         # Notify網址 
    headers = {"Authorization": "Bearer " + token}        # HTTPS表頭
    payload = {"message": message}                        # HTTPS內容
    image = open(image, "rb")
    imageFile = {"imageFile": image}                      # 設定圖片來源
    requests.post(url, headers=headers, 
                  data=payload, files=imageFile)          # 提出POST請求
    

# 發送圖片
token = '''你的token'''     # 你的token
message = "\n%s的美金\n買入為%s，賣出為%s" %(yesterday, usd_currency[0], usd_currency[1])
img = "bankcurrency.jpg"
notify(message, token, img)


