# input and output 
# var=eval(input("enter message :: "))
# print(var)
# print(type(var)) # defult input store string value


#int b=>1,2,3
#float b=>1.2,3.1
#dictionary b=>{'a':'jigar'}
#list=[1,2,3]
#tuple=(1,2,3)
#set={1,2,3}
# var=eval("{}")
# print("hello","word","khush","=============1")
# print("hello","word","khush","=============2",sep="/")
# print("hello",end=" di ") # we used same line print "end "fun give value its print 
# print("world")
#list into------------------------ 
l=['a','x','b','v',1,2,3,4,5,12,32]
# print(l[-5:-3],"here====") # why gives []  because start index > end index then give result else return []  `` 
# print(l[:6:2])
# l[3]=7 # --replace 
# l.insert(3,0) # insert
# print(l[1:])
# l.sort(reverse=True)
# l.reverse()
# print(l)
# last here ===== 16/10/24
# tuple
# t=(1,2,4,2,"kkk")
# p=tuple([1])
# print(type(p))
# print(p)


# test
# m1=input()
# m2=input()
# m3=input()
# l=[m1,m2,m3]
# print(l)
# print(type(l))
# check polindrom or not
# l=list(input())
# cl=l.copy()
# cl.reverse()
# if l==cl:
#     print("palindrom",cl)
# else:
#     print("not palindrom",cl)

# number of count a 
t=['d',"a","b",'c','c','a','a']
# print(t.count('a'))
# t.sort()
# print(t)

# dict={"name":"khush","animals":{"cat":1,"horse":2}}
# print(dict.items())

# dict={
#     m1:m1,
#     "sub2":m2,
#     "sub3":m3
# }
# print(dict)

# stor 9 and 9.0 in set
s={9.0,9.1}
# s={9,"9.0"}
# s={ 
#     (9.0),
#     (9)
# }
# s[0]=3
# print(s)
# a=9
# b=6
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print("no")
a=3
while a<10:
    print(a)
    a+=1

exit()
# for i in b:
#     print(i)

#! file opration  
f=open("demo.txt","r")
# f.write("i am khush t /n this khush line")
new=f.read()
nd=new.replace("khush","dipali")

# print(nd,"========herer")
f.close()
with open("demo.txt","w") as al:
    al.write(nd)

# search char---
with open("demo.txt","r") as al:
    m=al.read()
#     if m.find("boys")!=-1: 
# #?-1 is a fixed return value used by the find method to indicate that a substring was not found. It doesn't change based on the substring being searched for or the string being searched in.
#         print("found")
#     else:
#         print("nf")


#? class and object 
class a():
    "i am khush"
    va=10
    def fun():
        return "hello"
    def __init__(self,a,b): #! constructor
        print(a,"",b,"--")

# print(a.fun())
# ? oprator
#! bitwise and mean 4 and 5  is convert binary  and add convert into dec  ----bitwiseand ,bitwiseor,xor,right and left shift
x = 4
x &= 3

# print(x)

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c",'d',"khush","khush"])

# print(mylist)

str1="khush"
str2="01245"

# str2=str1.join(str2)
# repr(str2)

# unicode_1 = ("\u0123", "\u2665", "\U0001f638", "\u265E", "\u265F", "\u2168")  
# repr (unicode_1)

#! modules & abstaraction
#? perdefined modules
# import keyword
# print(keyword.kwlist)
# user defined modules
# import user_module
# print(user_module.sum(5,7))
# print(user_module.min(5,7)) # abstaraction

#! inhertance 
#!single 
class a:
    vara=10
    print("this is parent class ",vara)
class b(3):
    varb=30
    print("this is child class ",varb)

#!multline 
class c():
    print("this base child class---c--")

#! multipal
class d(a,b):
    print("this mulipal class---c--")
d()

# 1)
# *
# **
# ***
# ****
# *****

# 2)
# ******
# *****
# ****
# ***
# **
# *

#3)
# 666666
# 55555
# 4444
# 333
# 22
# 1 

# 4)
# 0
# 01
# 012
# 0123
# 01234

# (6)
# 6
# 66
# 666
# 6666
# 66666

# 7)
# 1 
# 3 2 
# 6 5 4
# 10 9 8 7

# 8)
        # * * * * * * 
        #  * * * * * 
        #   * * * *
        #    * * *
        #     * *
        #      *