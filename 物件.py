import math

class Circle:
    #建構式的第二個參數是用來接收傳入的半徑
    def __init__(self,radius):
        #利用self參數建立儲存資料的參數
        self._radius=radius
    #這個方法用來取得半徑
    def get_radius(self):
        #回傳類別內部變數的值
        return self._radius
    #這個方法用來設定半徑,第二個參數用來傳回半徑
    def set_radius(self,radius):
        #把半徑存入類別內的變數
        self._radius=radius
    #這個方法用來取的圓面積
    def get_area(self):
        #利用類別內部的變數計算圓面積,然後傳回結果
        return math.pi*self._radius*self._radius
    #這個方法用來取的圓周長
    def get_perimeter(self):
        #利用類別內部的變數計算圓周長,然後傳回結果
        return 2*math.pi*self._radius
#建立一個circle物件 設定給c1
c1=Circle(3)
print('半徑:',c1.get_radius())
print('園面積:',c1.get_area())
print('周長:',c1.get_perimeter())

#建立第二個circle物件,設定給c2,然後改變他的半徑
#再顯示他的半徑,面積和周長 
c2=Circle(5)
c2.set_radius(7)
print('半徑:',c2.get_radius())
print('園面積:',c2.get_area())
print('周長:',c2.get_perimeter())
#%%汽車類別
class Cars:
    
    #建構式
    def __init__(self,color,seat):
        #顏色屬性
        self.color=color 
        #座位屬性
        self.seat=seat
        
    #方法
    def drive(self):
        print(f"MY CAR IS {self.color} AND {self.seat} SEATS.")

class Motorcycle:
    pass

        
#建立CARS類別的物件
mazda= Cars('blue',4)

print(isinstance(mazda,Cars))
mazda.drive()
#%%類別屬性
class Cars:
    door=4
    #建構式
    def __init__(self,color,seat):
        #顏色屬性
        self.color=color 
        #座位屬性
        self.seat=seat
        self.weight=140
mazda=Cars('blue', 5)
toyota=Cars('red',7)
print('mazda door value',mazda.door)
print('toyota door value',toyota.door)
Cars.door=8
print('mazda door newvalue',mazda.door)
print('toyota door newvalue',toyota.door)
#%%實體方法
class Cars:
    
    #建構式
    def __init__(self):
        #顏色屬性
        self.color='blue'
    #實體方法
    def drive(self):
        print(f'{self} is {self.color}')
        #呼叫其他方法
        self.message()
    def message(self):
        print('Message method id called')
        
mazda=Cars()
mazda.drive()
#%%實體方法
class Cars:
    door=4
    #實體方法
    def drive(self):
        self.__class__.door=5
print('original',Cars.door)
mazda=Cars()
mazda.drive()
print('cars new door',Cars.door)
#%%類別方法
class Cars:
    door=4
    #建構式
    def __init__(self,color,seat):
        #顏色屬性
        self.color=color 
        #座位屬性
        self.seat=seat
    #箱型車
    @classmethod
    def van(cls):#cls class的簡寫
        return cls(6,'black')
    #跑車
    @classmethod
    def sports_car(cls):
        return cls(4,'yellow')
van=Cars.van()
sports_car=Cars.sports_car()
#%%靜態方法
class Cars:
    #速率靜態方法
    @staticmethod
    def speed_rate(distance,minute):
        return distance/minute
    
#透過物件呼叫
van=Cars()
van_rate=van.speed_rate(10000,20)
print('van rate',van_rate)

#透過類別呼叫
sports_car_rate = Cars.speed_rate(20000,20)
print('sports car rate',sports_car_rate)
#%%私有屬性
class Circle:
    PI=3.14
    def __init__(self,r=1):
        self.__radius=r
    def getRadius(self):
        return self.__radius
    def getArea(self):
        return self.PI*self.__radius*self.__radius
c1=Circle(10)
print('半徑:',c1.getRadius())
print('面積:',c1.getArea())

class Blog:
    #建構式
    def __init__(self):
        self.__author='Mike'
        self.__titles=[]
    def __add_post(self,title):
        self.__titles.append(title)
blog=Blog()
#這會出錯因為這是私有，不能直接抓
# print(blog.__author)
#但是python的私有不是真的私有,還是可以抓的到
print(blog.__dict__)#透過dict來查看
print(blog._Blog__author)#根據上面可知用這個方式還是可以呼叫出來

#%%繼承
class Transportation:
    #建構式
    def __init__(self):
        self.color='white' #顏色屬性
    #駕駛方法
    def drive(self):
        print('drive method is called')
#汽車類別
class Car(Transportation):
    #加速方法
    def accelerate(self):
        print('accelerate method is called')
#飛機類別
class Airplane(Transportation):
    #飛行方法
    def fly(self):
        print('fly method is called')

mazda=Car()
mazda.drive()
print(mazda.color)
#%%覆寫
class Employee:
    #這個初始化方法用來設定員工的姓名
    def __init__(self,name):
        self.__name=name
    #這個方法用來傳回員工姓名
    def getname(self):
        return self.__name
    #這個方法用來傳回員工本月薪水
    def getSalary(self,hours,payrate):
        return hours *payrate
class SalesPerson(Employee):
    #這個方法用來傳回銷售人員本月薪水(含業績獎金)
    def getSalary(self,hours,payrate,bonus):
        return hours *payrate+bonus
E1=Employee('小丸子')
E2=SalesPerson('小紅豆')
print('員工',E1.getname(),'的本月薪水為',E1.getSalary(120,150))
print('銷售人員',E2.getname(),'的本月薪水為',E2.getSalary(120,150,3000))






















