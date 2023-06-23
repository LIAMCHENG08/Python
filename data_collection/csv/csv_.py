import csv

#bom的encoding是utf-8-sig
with open('csv_bom.csv',encoding=('utf-8-sig')) as f:
    csv_reader=csv.reader(f)
    list_rp=list(csv_reader)
print(list_rp)
#%%
#檔案編碼跟python預設的ansi一樣，或語系是中英，就不需要打encoding,
#檔案編碼需一致
with open('csvsample.csv',encoding=('utf8')) as f:
    csv_reader=csv.reader(f)
    list_rp=list(csv_reader)
print(list_rp)

print(list_rp[1])
print(list_rp[2][1])
#%%
print(list_rp[:][1])#想抓account,不能這樣用，看似很合邏輯
print(list_rp[1])#跟上面輸出的結果一樣
#%%
for i in list_rp:#只能用迴圈的方式
    print(i[1])
    
for i in list_rp:
    print(i[1:3])
    
for i in list_rp:
    print(i[0:3:2])
for i in list_rp:
    print(i[0],i[2])

# for i in list_rp:#不能這樣用
#     print(i[0][2])
#%%
import csv

fn='csvsample.csv'
with open(fn,'w',newline='',encoding=('utf-8')) as f:
          csv_writer=csv.writer(f,delimiter='\t')#delimiter是放在這,csv預設以逗號分隔，想改預設就可以用delimiter這函數
          csv_writer.writerow(['姓名','電話','ID','費用','是否前往'])#writerow都是用list,以，區隔
          csv_writer.writerow(['小明','(02)222222','A123456789',100,True])#裡面可以放字串、數值、bool
          csv_writer.writerow(['小美','(02)111111','A123458888',200,False])
          
with open(fn,encoding=('utf8')) as file:
    csvReader=csv.reader(file)
    listReport=list(csvReader)