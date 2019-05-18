

a=open("date.txt",'r',encoding='utf-8')

# print(a.read())
# print(a.readline())

# a.readlines()[0]
for i in a.readlines():
    print(i)
a.close()