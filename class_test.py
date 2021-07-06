class student :
    name = ''
    age = 0

    def __init__(self,n,a):
        self.name=n
        self.age=a

students = []

student1 = student('udichi',12)
students.append(student1)
student2 = student('ranu', 10)
students.append(student2)
student3 = student('khushi',11)
students.append(student3)
student4 = student('rashi',8)
students.append(student4)
student5 = student('appu',12)
students.append(student5)
student6 = student('swara',13)
students.append(student6)
student7 = student('bhakti',11)
students.append(student7)
student8 = student('uttara',12)
students.append(student8)

for x in students:
    print('name of the student is '+x.name+ 'and her age is ',x.age )