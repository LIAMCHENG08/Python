import xml.etree.ElementTree as et#匯入套件
tree=et.ElementTree(file=('menu.xml'))#取的物件，函數裡面一定要放file=
root=tree.getroot()#取得root物件
print(root.tag)#輸出root物件的tag屬性，得到menu

for child in root:#child為變數可任意命名
    print('tag:',child.tag,'attributes:',child.attrib)
    for grandchild in child:#grandchild為變數
        print('\ttag:',grandchild.tag,'attributes',grandchild.attrib)

print(len(root))#輸出菜單項目
print(len(root[0]))#早餐項目數
#%%
import xml.etree.ElementTree as ET
tree=ET.parse('country_data.xml')
#parse跟上面ElementTree一樣，只是不用加file
root = tree.getroot()#獲得根節點
for country in root.findall('country'):#找出所有country
    rank=int(country.find('rank').text)
    #text找的是rank得value，找到得value是字串，所以轉成int
    if rank>50:
        root.remove(country)
        #是用root
tree.write('xmloutput.xml',encoding=('utf-8'))

    