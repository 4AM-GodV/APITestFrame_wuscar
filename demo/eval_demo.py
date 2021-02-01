
sum = eval("66+32")
print(sum)

#  字符串转字典

print(eval("{'name':'linux','age':18}"))


#  eval传值

print(eval("{'name':'linux','age':age}",{"age":18}))


#  优先传本地的值
age = 25
print(eval("{'name':'linux','age':age}",{"age":18},locals()))




