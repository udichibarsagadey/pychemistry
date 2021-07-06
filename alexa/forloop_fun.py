"""sum=0
for n in range(9999):
    print(n)
    print("udichi")

    sum=sum+n
    print("udichi")
print("sum of numbers:",sum)
print("i'm outside the loop")

add=0

start=int(input("enter start point"))
end=int(input("enter start point"))

for odd in range(start,end):
    reminder= odd%2

    if reminder!=0:
        add=add+odd

print("the addition of odd number is:",add)
"""
