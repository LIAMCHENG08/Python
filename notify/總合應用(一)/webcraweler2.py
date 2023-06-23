import MySQLdb
import pandas as pd
from datetime import date
import datetime

# ==============================
#      到資料庫找出前一日美金買入及賣出匯率
# ==============================

def show_usd_currency():
    # 取得昨日日期
    today = date.today()
    yesterday = today + datetime.timedelta(days = -1)
    
    try:
        # 開啟資料庫連接
        conn = MySQLdb.connect(host="localhost",     # 主機名稱
                                user="marin",        # 帳號
                                password="1qazxsw2", # 密碼
                                database = "testdb1", #資料庫
                                port=3306,           # port
                                charset="utf8")      # 資料庫編碼
        
        # 使用cursor()方法操作資料庫
        cursor = conn.cursor()
        
        # 查詢表格taiwanbank_currency的美金買入及賣出價
        try:
            sql = """SELECT buy, sold FROM taiwanbank_currency WHERE currency LIKE '%s' and date='%s'""" %(("美金"+"%"), yesterday)
            cursor.execute(sql)
            data = cursor.fetchone()

            return data
           
        except Exception as e:
            print("錯誤訊息：", e)
     
    
    except Exception as e:
        print("資料庫連接失敗：", e)
        
    finally:
        conn.close()
        print("資料庫連線結束")