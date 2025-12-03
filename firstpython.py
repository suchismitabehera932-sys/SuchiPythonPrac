#1.Write a python program to take a string input and convert the first letter to uppercase.
from html.parser import endtagfind
from pickletools import markobject

st="suchismita behera"
print(st.capitalize())

#2.How would you convert a string "python programming" into all uppercase letters.
st="python programming"
print(st.upper())

#3.write code to transform the string"HELLOW WORLD" into all lowercase.
st="HELLOW WORLD"
print(st.lower())

#4.convert the string "learning python is fun" into title case using title().
st="learning python is fun"
print(st.title())

#5.write a program to find the length of a string "Data Science" using?
st="Data Science"
print(len(st))

#6.How would you count how many times letter"a" appears in "banana"?
st="banana"
print(st.count("a"))

#7.How can you check weather a password string like"mypassword" is in all lowercase letters?
st="mypassword"
print(st.islower())

#8.Take the sentence "python is easy and python is powerful" and count how many "python" occurs.
st="python is easy and python is powerful"
print(st.count("python"))

#9.Write the code to make the string"good morning" appear as "Good morning".
st="good morning"
print(st.capitalize())

#10. What will be the output of "hello world".title()?
st="hellow world"
print(st.title())

#11. How do you find out the totall number of charachers(including spaces) in the string "Artifitial Intelligence"?
st="Artificial Intelligence"
print(len(st))

#12.Given "python",explain the difference in result between "PYthon".upper() and "PYthon".capitalize().
st="PYthon"
print(st.upper())
#means it coverts all the characters in to uppercase.
st="PYthon"
print(st.capitalize())
#means it converts 1st letter should be capital.

str1="python is very simple"
l1=str1.split()
print(l1)
print(l1[::-1])

#nohtype si ysae dna elmis
#Nested list - one list under multiple list rehtahe
l1 = [10,'python',5.5]
l2=[20,30,'world','false']
l3=[1,'true',5,'java']
nested =[l1,l2,l3]
print(nested)
print(nested[1])
print (nested[0])
print(nested[1][0])
print(nested[2][2])

#NESTED RELATED QUESTION FOR PRACTICE

numbers=[[1,2,3],[4,5,6],[7,8,9]]
#Q1. print the number 5
print(numbers[1][1])

fruits=[['apple','banana'],['mango','grapes']]
#Q2. change 'banana' to orange.
fruits[0][1]='orange'
print(fruits)

nested=[[1,2],[6,7],[9,10]]
#Q3. how many sublists are there
print(len(nested))

nested=[[10,20],[30,40],[50,60]]
#Q4. print 60
print(nested[-1][-1])

# print 30
print(nested[-2][0])

#print 20
print(nested[0][-1])

nested=[[1,2],[3,4],[5,6]]
#Q.5 REPLACE [3,4] WITH [7,8]
nested[1]=[7,8]
print(nested)


s="python programming"
count_p= s.count('p')
print(count_p)

l1=['python','is','fun']
l2=' '.join (l1)
print(l2)

l=[10,20,30,40]
l.insert(2,25)
print(l)

l=[10,20,30,40,30]
l.remove(30)
print(l)

l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)

l=[10,20,30]
l.clear()
print(l)

s={1,2,3,4}
s.remove(3)
print(s)

s={10,20,30}
s1={20,30,40}
s3=s.intersection(s1)
print(s3)

s={1,2,3,4}
s1={3,4,5}
s3=s.difference(s1)
print(s3)

d={'a':1,'b':2}
d['c']=3
print(d)

d={'a':1,'b':2,'c':3}
d.pop('b')
print(d)

d={'x':10,'y':20}
keys=d.keys()
print(keys)

d={'name':'ravi','age':25,'city':'delhi'}
d.pop('name')
print(d)

keys=['a','b','c']
values=[1,2,3]
d=dict(zip(keys,values))
print(d)

#IF ELSE CONDITIONAL STATEMENT--------DT--10 OCT

# age = int(input('enter your age:'))
# age1=19
# if age<18:
#     print('you are eligible for vote.')
#
#  #using string
# age=int(input('enter your age:'))
# s=input('enter your string:')
# if age<18:
#     print('you are eligible for vote.')
#
# #age=int(input('enter your age:'))
# age=18
# if age >=18:
#     print('you are eligible for vote.')
#
# age=int(input('enter your age:'))
# if age>=25:
#     print('you are eligible for 10 lakes package.')

# age=eval(input('enter your age:'))
# if age>=25:
#     print('you are eligible for 10 lakes package.')

# a=int(input("enter a number"))
# b=int(input("enter another number"))
# if a>b:
#     print("a is greater than b")

#IF ELSE CONDITION STATEMENT---------11OCT
# age = 16
# if age >= 18:
#     print("you are not eligible to vote.")
# else:
#     print("you are eligible to vote.")

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# if num1>num2:
#     print('number1 is greater than number 2')
# else:
#     print('number2 is greater than number 1')

# int (input("enter yor marks"))
# if age >=40:
#     print("you are not eligible to pass.")
# else:
#     print("you are eligible to pass.")

# s= input('enter the world')
# s1=len(s)
# if len(s)>=5:
#     print(s.upper())
# else:
#     print(s.lower())

# num= int(input('enter the number'))
# if num%2==0:
#     print(num,'is even')
# else:
#     print(num,'is odd')

# s1=int(input('enter the number'))
# if s1%3==0 and s1%5==0:
#     print('fizzbuzz')
# else:
#     print('buzz')

# hi=input('enter the word:')
# if hi[0] in ['a','e','i','o','u','a']:
#     print('vowel word')
# else:
#     print('not a vowel')

# 1. Check if a string is palindrome or not.
# a=input("enter your name")
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")
#
# # 2. Replace all spaces in a string with “_”.
#
# s="i am a good girl"
# s2=s.replace(" ","_")
# print(s2)
#
# # 3. Find the first and last character of a string.
#
# s="hello everyone"
# print("first:",s[0])
# print("last:",s[-1])
#
# # 4. Count how many times a specific word appears in a sentence.
#
# s="python programming"
# s2="programming"
# s3=s.count(s2)
# print(s3)
# s3=s.index(s2)
# print(s3)
#
# # 5. Check if a string contains only alphabet characters.
#
# s="apple"
# if s.isalpha():
#     print("only alphabet")
#
# # 6. Find the largest and smallest number in a list.
#
# s1=[25,28,95,35,100,105]
# print(max(s1))
# print(min(s1))

# # 7. Find the second highest number in a list.
#
# s1=[40,50,75,95,115]
# s1.sort()
# print("second highest:",s1[-2])
#
# # 8. Check if a list is sorted in ascending order.
#
# s1=[1,2,3,4,5]
# if s1== sorted(s1):
#     print('list is sorted')
# else:
#     print('list is not sorted')
#
# # 9. Check if a value exists in a tuple.
#
# t1=(30,23,45,78)
# t2=45
# if t2 in t1:
#     print("value exists")
# else:
#     print("value doesn't exist")
#
# 10. Convert a tuple to a list and add a new element.

# s=(56,78,35,98)
# s2=list(s)
# s2.extend([12,67,90])
# print(s2)
#
# # 11. Find the sum of all numbers in a tuple.
#
# s=(6,7,8,9)
# print(sum(s))

# # 12. Create a nested tuple and access inner values.
# s1=((5,6),(6,7),(8,9))
# print(s1[1][1])
#
# # 13. Convert a tuple of strings into one single string
#
# t=("Hello","World","Python")
# t2="- ".join(t)
# print(t2)

# # 14. Find the maximum and minimum value in a tuple.
#
# t1=(78,56,45,90,34)
# print(max(t1))
# print(min(t1))


# PRACTICE-------------
# s=int(input("enter a number"))
# if s%2==0:
#     print("even")
# else:
#     print("odd")

# s=int(input("enter a age"))
# if s>=18:
#     print("eligible for vote")
# else:
#     print("eligible not for vote")

# s1=int(input('enter a number:'))
# if s1%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")

# s1=input("enter a character:")
# if s1 in["a","e","i","o","u"]:
#     print("vowel")
# else:
#     print("consonant")

# s1=int(input('enter first number:'))
# s2=int(input('enter second number:'))
# if s1 > s2:
#     print("s1 is greater than s2")
# else:
#     print("s2 is greater than s1")

# a=int(input("enter a year"))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("leap year")
# else:
#     print("not leap year")

# s1=int(input('enter a number'))
# if s1%2!=0 and s1>10:
#     print("yes it is")
# else:
#     print("no")

#PYTHON CLASS--------------15TH OCTOBER
# s=int(input("check grade"))
# if s>80:
#     print("grade a")
# elif s>70:
#     print("grade b")
# elif s>60:
#     print("grade c")
# else:
#     print("not pass")

# colour=input("enter the colours")
# if colour=='red':
#     print("stop")
# elif colour=='yellow':
#     print("move to the trafic")
# elif colour=='green':
#     print("move")
# else:
#     print("enter the valid colour")

# a=int(input("enter the  number"))
# b=int(input("enter the  number"))
# c=int(input("enter the  number"))
# if a>b and a>c:
#     print("a is greater ")
# elif b>a and b>c:
#     print("b is greater ")
# elif c>a and c>b:
#     print("c is greater ")
# else:
#     print("a is less ")

# s1=int(input('enter a number'))
# if s1 % 2 == 0 and s1 % 3 == 0:
#     print("number is divisible by both 2 and 3")
# elif s1 % 2 == 0:
#     print("number is divisible by 2")
# elif s1 % 3 == 0:
#     print("number is divisible by 3")
# else:
#     print("number is not divisible by 2")

#NESTED IF ELSE STATEMENT------------

# s1=input("enter a character")
# if s1.isdigit():
#     print("number is digit")
# elif s1.isalpha():
#  if s1.islower in ['a','e','i','o','u']:
#         print("its a vowel")
#  else:
#         print("its a consonant")
# else:
#     print("its a special character")


#PYTHON PRACTICE IF ELIF ELSE PROGRAM---------

# s1=int(input('enter their marks 0-100'))
# if s1>=90 and s1<=100:
#     print("grade A")
# elif s1>=80:
#     print("grade B")
# elif s1>=70:
#     print("grade C")
# elif s1>=60:
#     print("grade D")
# elif s1>=0:
#     print("grade F")
# else:
#     print("invalid grade marks must be between 0 and 100")


# s1=int(input('enter their marks 0-100'))
# if s1>=90 and s1<=100:
#     print("grade A")
# elif s1>=80 and s1<=89:
#     print("grade B")
# elif s1>=70 and s1<=79:
#     print("grade C")
# elif s1>=60 and s1<=69:
#     print("grade D")
# elif s1<60:
#     print("grade F")
# else:
#     print("invalid grade marks must be between 0 and 100")
#
#
# s1=int(input('enter the current hour 0-23'))
# if s1>=5 and s1<=11:
#     print("good morning")
# elif s1>=12 and s1<=17:
#     print("good afternoon")
# elif s1>=18 and s1<=21:
#     print("good evening")
# else:
#     print("other wise")
#
# s1=int(input('enter first number:'))
# s2=int(input('enter second number:'))
# s3=int(input('enter third number:'))
# if s1 >= s2 and s1 >= s3:
#     print("largest number is s1")
# elif s2 >= s1 and s2 >= s3:
#     print("largest number is s2")
# else:
#     print("largest number is s3")
#
#
# w= int(input("enter a year")
# if w%4==0 and w%400==0:
#     print("its a leap year")
# else:
#     print("its not leap year")
#
# PYTHON NESTED IF ELSE STATEMENT------------------
# s1=input("enter a character")
# if s1.isdigit():
#     print("number is digit")
# elif s1.isalpha():
#  if s1.islower in ['a','e','i','o','u']:
#         print("its a vowel")
#  else:
#         print("its a consonant")
# else:
#     print("its a special character")

# num=-1
# if num>0:
#     print("positive number")
#     if num%2==0:
#         print("even number")
# else:
#     print("not satisfied the condition")

# username="admin"
# password="1234"
# if username=="admin":
#     if password=="1234":
#         print("login successfully")
# else:
#     print("login failed")

# s1=int(input("electricity units used"))
# if s1<=50:
#     bill=s1*2
# else:
#     if s1<=100:
#         bill=(50*2)+(s1-50)*3
#     else:
#         bill=(50*2)+(50*3)+(s1-100)*5
# print("total electricity bill:",bill)


# NESTED IF PROGRAM PRACTICE---------------------------

# s1=int(input("enter a number"))
# if s1>0:
#     if s1%2==0:
#         print(s1,'is even')
#     else:
#         print("not even")
# else:
#     print("not a positive number")
#

# s1=int(input('enter a number'))
# id=input("input you have id")
# if s1>18:
#     if id.lower()=="yes":
#         print('yes')
#     else:
#         print('no')
# else:
#     print('yes')

# FOR LOOP -------------------

# for ch in "hello world":
#     print(ch)

# for num in range(1,6):
#     print(num)

# using list
# for ch in [10,20,30]:
#     print(ch)

# for ch in "suchismita behera":
#     print(ch)

# for i in range(5):
#     print("suchismita behera")

# for i in range(1,20):
#    if i%2==0:
#        print(i)
#
# l1 =[10,20,30,40,50]
# sum =0
# for ele in l1:
#     sum += ele
# print(sum)

#WHILE FUNCTION-----------
# i=0,1
# while i<=5:
#     print(i)
#     i+=1

# i=0
# total=0
# while(i<=5):
#     total+=i
#     i+=1
# print(total)

# i=10
# while i>0:
#     print(i)
#     i=i-1

# i=1
# while i<=10:
#     print(5*i)
#     i=i+1

# Print numbers from 1 to 10 using a while loop.
# i=10
# while i <=10:
#     print(i)
#     i=i+1

# Print even numbers between 1 and 20.
# i=2
# while i<=20:
#     print(i)
#     i=i+2

# Print odd numbers between 1 and 15.
# i=1
# while i<=15:
#     print(i)
#     i=i+2

# Print numbers in reverse from 10 to 1.
# i=10
# while i>=1:
#     print(i)
#     i=i-1

# Print the first 10 natural numbers and their squares.
# i=10
# while i<=10:
#     print("numbers",i,"square",i*i)
#     i=i+1

# Print the multiplication table of 5 using a while loop.
# i=1
# while i<=10:
#     print("5 x",i,"=",5*i)
#     i=i+1

# Print your name 5 times using a while loop.
# i=1
# while i<=5:
#     print("suchismita")
#     i=i+1

# Find the sum of first 10 natural numbers.

# Find the sum of all even numbers between 1 and 20.

# Print all numbers divisible by 3 between 1 and 30.
# i=1
# while i<=30:
#     if i % 3 == 0:
#         print(i)
#         i = i + 1

# PYTHON CLASS ---------------------------------24TH OCTOBER
# LOOP CONTROL STATEMENT---------------BREAK

# for i in range(1,5):
#     if i==1:
#         break
#     print(i)

# for i in range(1, 11):
#     if i%2 == 0:
#         continue
#     print(i)

# i=1
# while i<11:
#     if i%2==0:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
#
# i = 1
# while i < 11:
#     if i % 2 == 0:
#         i = i + 1
#         break
#     print(i)
#     i = i + 1
#
# i=1
# while i < 11:
#     if i % 2 == 0:
#         pass

# for i in range(1,10):
#     if i==6:
#         break
#     print(i)

# for i in range(1,10):
#     if i==6:
#         continue
#     print(i)
#

# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i)
#
# for i in range(1,10):
#      if i % 7 == 0:
#          break
#      print(i)
#
# for i in range(1,10):
#      if i % 9:
#         print("found")
#      print(i)



# PYTHON PROGRAM USING FUNCTION-------------------KRISHNA SIR
# Write a python program add two number,substraction,division.
# def cal(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
#
# def swap_two_num(a,b):
#     b=a-b
#     a=a-b
#     return a,b
#
# def convert_c_f(celcious):
#     fahrenheit=celcious*9/5+32
#     return fahrenheit




def decor(cal):
    def sub(a,b):
        sub=a-b
        return sub,cal(a,b)
    return sub



@decor

def cal (a,b):
    add=a+b
    return add
print(cal(10,20))

....




