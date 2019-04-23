# a={3,1,2}
# print(a)
# print(type(a))
#
# a.clear()
# print(a)

# a=[5]
# a.clear()
# print(type(a))
# print(a)
#
# a={'a':4,'b':5,'c':'abc'}
# print(a)
#
# b={1:2,'b':5,'c':'abc'}
# print(b)
# print(a.keys())
# print(b.values())
# print(a.items())

# a = []
# for i in range(1, 100):
#      print("数字是" +i)
#     print("数字是%d"%i)
#     a.append(i)

a = input("请输入一个数字")
if int(a) > 0:
    print("您输入的数字大于0")
elif int(a) ==0:
    print("您输入的数字等于0")
else:
    print("您输入的数字小于0")
