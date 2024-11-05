# print("Hello Word!")
# a=2
# b=3.2
# c=a+b
# print(c)
# (type(a))
# print(type(b))
# d='abcdef'
# print(type(d))
# e=[1,2,3,4]
# print(type(e))
# num1=input('please enter the first number')
# num2=input('please enter a second number')
# print(num1,num2)
# print(type(num1))
# print (type(num2)) 
# bill_total=19  
# discount=10
# if bill_total>100:
#     print("bill is greater than 100!")
#     bill_total=bill_total-discount
# else:
#     print("bill is less than 100")    
# print("total bill:"+str(bill_total))   
# print(type(bill_total))
# my_global=10
# def fn1():
#     enclosed_v=8
#     def fn2():
#         local_v=5
#         print('Access to global',my_global)
#         print('Access to global',enclosed_v)
# print(fn1())

# print(enclosed_v)
# print(local_v)
# text="random string with a lot of characters"
# print(text[-1])
# file_counts={"jpg":10,"txt":14,"csv":2,"py":23}
# for extension in file_counts:
#  print(extension)
# for ext,amount in file_counts.items():
#  print("there are {} files with the .{} extension".format(amount,ext))
# cool_beasts={"octopuses":"tentacles","dolphins":"fins","rhinos":"horns"}
# for extension in cool_beasts:
#     print(extension)
# for ext,amount in cool_beasts.items():
#     print(" {} have .{} extension".format(amount,ext))
# a=5/0
# print(a)
# def divide_by(a,b):
#     return a/b
# try:
#     ans=divide_by(10,0)
# except:
#     print("something went wrong!")
# def divide_by(a,b):
#     return a/b
# try:
#     ans=divide_by(10,0)
# except Exception as e:
#     print("something went wrong!",e)
#     print(e.__class__)
items=[1,2,3,4,5]

try:
        item=items[6]
        print(item)
except:
        print("item not found")
# menu=["espresso","mocha","cappuccino","cortado","americano"]
# def find_coffee(coffee):
#     if coffee[0]=='c':
#         return coffee
    
# map_coffee = map(find_coffee,menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)
