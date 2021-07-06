"""
creating alexa
*print
*variables
*input
"""
name =input('write your name here ')
print(name)

num1 =int(input('write your 1st fav  num '))
num2 =int(input('write your 2nd fav num '))
num3=int(input('write your 3rd fav num '))

add = num1+num3+num2
sub = num1-num3-num2
mul = num1*num3*num2
div = num1/num3/num2
print(num1)
print(num2)
print(num3)
print(add)
print(sub)
print(mul)
print(div)

print('________________________________')

num1 =int(input('write your 1st fav  num '))
num2 =int(input('write your 2nd fav num '))
QUE =input('enter the operation be performed  : ')

if QUE =="+":
    add=num1+num2
    print(add)
if QUE =="-":
    sub=num1-num2
    print(sub)
if QUE =="*":
    mul=num1*num2
    print(mul)
if QUE =="/":
    div=num1/num2
    print(div)