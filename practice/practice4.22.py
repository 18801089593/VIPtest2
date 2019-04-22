# 1、	逆序存放：s.reverse()---改变原来元组的值
# 2、	排序存放：s.sort()------改变原来元组的值
# 3、	排序：sorted(s)---------不改变原来元组的值，只返回一个排序结果
# 4、	插入：s.insert(n,m)-----在某一位置(s[n]前面)插入该值m
# 5、	追加：s.append(n)-------在该元组末尾追加n


# a=[1,2,3.3,4,5,6,7,'much']
# print(a)
# print(type(a))
# print(a[2])
# print(a[1:5])
# print(a[1:5:2])
# print(a[-1])

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b[-3])
# print(b[3:8:2])
# b.reverse()
# print(b)

b = [9, 2, 5, 4, 3, 6, 7, 8, 1]
# b.sort()
# print(b)

# print(sorted(b))
# print(b)
# b.append(11)
# print(b)

list=[]
for i in range(1,10):
    # print(i)
    list.append(i)
print(list)




