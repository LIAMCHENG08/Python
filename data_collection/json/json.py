import json
f1='json_object_bom.json'
f2='json_array.json'

with open(f1,encoding=('utf-8-sig')) as file:
    data=json.load(file)
print(data)

# with open(f2) as file:
#     data2=json.load(file)
# print(data2)
#%%
import json
dictobject={'x':60,'y':100,'z':90}
fn='json_object_ansi.json'
with open(fn,'w')as f:
    json.dump(dictobject,f)
    
listarray=[{'x':'一二三','y':101,'z':90},{'a':10,'b':15,'c':30}]
f3='json_array.json'
with open(f3,'w')as farrary:
    json.dump(listarray,farrary,ensure_ascii=False)
    