'''
Python练习题：
1、打印小猫爱吃鱼，小猫要喝水
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''

# class Cat():
#     def __init__(self,name):
#         self.catname=name
#     def eat(self):
#         print("%s爱吃鱼"%self.catname)
#     def drink(self):
#         print("%s要喝水"%self.catname)
#
# cat=Cat("小花猫")
# cat.eat()
# cat.drink()







class Boy():
    def __init__(self,name):
        self.boyname=name
    def run(self,count):
        if count>=0:
            #计算跑步次数后，减下来的重量
            changeweight=count*0.5
            return changeweight
        else:
            print("error")

    def eat(self,count):
        if count>=0:
            #计算吃东西增加的重量
            changeweight=count*1
            return changeweight
        else:
            print("error")

#打印出小明原体重75，吃3次东西，跑步5次后的体重
xm=Boy("小明")
sub=xm.run(5)
add=xm.eat(3)
now=75-sub+add
print("小明现在的体重是%s"%now)

# class House():
#     def __init__(self,initarea):
#         self.initarea=initarea
#
#     def type(self,hstype):
#         print("您的户型是%s"%hstype)
#
#     def area(self, area):
#         usedarea=0
#         for i in area:
#             usedarea+=i
#         remainarea=self.initarea-usedarea
#         print("剩余可用面积%s平方米"%remainarea)
#
#     def furniture(self,jiaju):
#         print("您的家具%s"%jiaju)

# myhouse={
#     '床':4,
#     '衣柜':2,
#     '餐桌':1.5
# }
# jiajulist=[]
# for i in myhouse.keys():
#     jiajulist.append(i)
# mjlist=[]
# for j in myhouse.values():
#     mjlist.append(j)
# #print(jiajulist)
# house=House(100)
# house.type("花园型")
# house.furniture(jiajulist)
# house.area(mjlist)

# class solder():
#     def __init__(self,name,gun):
#         self.name=name
#         self.gun=gun
#     def fire(self):
#         print("%s使用%s开火"%(self.name,self.gun))
#
#     def sendzd(self,subnum):
#         print("%s发射子弹"%self.gun)
#         return subnum
#     def addzd(self,addnum):
#         print("%s装弹"%self.gun)
#         return addnum
#
# solder=solder("瑞恩","AK47")
# solder.fire()
# send=solder.sendzd(5)
# receiver=solder.addzd(8)
# initzd=6
# print("剩余子弹%d颗"%(initzd-send+receiver))
list=[3,1,29,17,8,27,87]
# for i in range(len(list)):
#     for j in range(i):
#         if list[j]>list[i]:
#             tmp=list[i]
#             list[i]=list[j]
#             list[j]=tmp
#     print(list)
min=0
max=len(list)-1
n=int(input("输入你想知道的值"))
while list[md] != n:
    md = (min + max) // 2

    if list[md] == n:
        print(md)
        continue
    elif list[md] > n:
        min = md
    elif list[md] < n:
        max = md

# for i in range(4):
#     print(i)
# #list=['a','b','c']
# newlist=[]
# for i in list:
#     newlist.append(str(i))
# print(newlist)
# new=",".join(newlist)
# print(new)
#
# file=open("data.txt",'w+')
# file.write(new)
# file.close()