# Chapter - 2 Practice set: Practice set:
# Question - 1:
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

print(f"The sum of two numbers are: {num1 + num2}")

# Question - 2:
x = int(input("Enter number 1: "))
z = int(input("Enter number 2: "))

print(f"The remainder when x is divided by z: {x % z}")

# Question - 3:
a = input("(A)Enter something here: ")
b = int(input("(B)Enter number here: "))
c = float(input("(C)Enter decimal number here: "))
d = bool(input("(D)Enter true of false here: "))

print(f"The type of a is; {type(a)} {a}")
print(f"The type of b is; {type(b)} {b}")
print(f"The type of c is; {type(c)} {c}")
print(f"The type of d is; {type(d)} {d}")

# Question - 4:
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(f"Is a is greater than b: {a > b}")

# Question - 5:
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(f"The average of two numbers are: {(num1 + num2)/2}")

# Question - 6:
number = int(input("Enter the number for square: "))

print(f"The square of the number entered by the user is: {number**2}")

# Chapter - 3 Practice set: Practice set:
# Question - 1:
username = input("Enter your name here: ")

print(f"Good Afternoon, {username}")

# Question - 2:
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Utkarsh").replace("<|Date|>", "21/07/2006"))

# Question - 3:
double = "hello   world" 
print(double.find("  "))

# Question - 4:
double = "hello   world" 
print(double.replace("   ", " "))

# Question - 5:
letter = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter)

# Chapter - 4: Practice set:
# Question - 1:
fruit_list = []

fruit_name = input("Enter fruit name 1: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 2: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 3: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 4: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 5: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 6: ")
fruit_list.append(fruit_name)
fruit_name = input("Enter fruit name 7: ")
fruit_list.append(fruit_name)

print(fruit_list)

# Question - 2:
marks_list = []
marks = int(input("Enter marks here: "))
marks_list.append(marks)
marks = int(input("Enter marks here: "))
marks_list.append(marks)
marks = int(input("Enter marks here: "))
marks_list.append(marks)
marks = int(input("Enter marks here: "))
marks_list.append(marks)
marks = int(input("Enter marks here: "))
marks_list.append(marks)
marks = int(input("Enter marks here: "))
marks_list.append(marks)

marks_list.sort()
print(marks_list)

# Question - 3:
a = ("utkarsh", 45, 123.123, True)
a[0] = "sharma"
print(a[0])

# Question - 4:
num_list = [1, 2, 3, 4]
print(sum(num_list))

# Question - 5:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

# Chapter - 5: Practice set:
# Question 1:
hindi_to_english = {
    "khana": "food",
    "pani": "water",
    "kutta": "dog",
    "jutta": "lier"
}

ask = input("Enter word to know the hinid translation: ")
print(f"The translation of hinid word into english is: {hindi_to_english[ask]}")

# Question - 2:
s = set()

num1 = int(input("Enter number 1: "))
s.add(num1)
num2 = int(input("Enter number 2: "))
s.add(num2)
num3 = int(input("Enter number 3: "))
s.add(num3)
num4 = int(input("Enter number 4: "))
s.add(num4)
num5 = int(input("Enter number 5: "))
s.add(num5)
num6 = int(input("Enter number 6: "))
s.add(num6)
num7 = int(input("Enter number 7: "))
s.add(num7)
num8 = int(input("Enter number 8: "))
s.add(num8)

print(s)

# Question - 3:
setu = {"18", 18}
print(setu)

# Question - 4:
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))

# Question - 5:
s = {}
print(type(s))

# Question - 6:
dict = {}

name = input("Enter your name: ")
language = input("Enter your language: ")
dict.update({name:language})

name = input("Enter your name: ")
language = input("Enter your language: ")
dict.update({name:language})

name = input("Enter your name: ")
language = input("Enter your language: ")
dict.update({name:language})

name = input("Enter your name: ")
language = input("Enter your language: ")
dict.update({name:language})

print(dict)

# Chapter - 6: Practice set:
# Question - 1:
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"The greatest number is: {num1}")

elif(num2>num1 and num2>num3 and num2>num4):
    print(f"The greatest number is: {num2}")

elif(num3>num1 and num3>num2 and num3>num4):
    print(f"The greatest number is: {num3}")

elif(num4>num1 and num4>num2 and num4>num3):
    print(f"The greatest number is: {num4}")

else:
    print("something went wrong")

# Question - 2:
'''total percentage = 44%
min marks = 33%'''

marks1 = int(input("Enter marsk here: "))
marks2 = int(input("Enter marsk here: "))
marks3 = int(input("Enter marsk here: "))
percentage = (100*(marks1 + marks2 + marks3))/300
total_percentage = round(percentage, 2)

if(total_percentage > 44 and marks1>33 or marks2>33 or marks3>33):
    print(f"You passed the exam and your percentage is: {total_percentage}")
else:
    print(f"You failed the exam and your percentage is: {total_percentage}")

# Question - 3:
word1 = "make a lot of money"
word2 = "buy now"
word3 = "subscribe now"
word4 = "click this"
message = input("Enter your message here: ")
if(word1 in message or word2 in message or word3 in message or word4 in message):
    print("Your message is marked has spam message")
else:
    print("Your message is clean as water")

Question - 4:
username = input("Enter your username here: ")
if(len(username)>=10):
    print("Username registered")
else:
    print("Your username doesn't contains enough chracters")

# Question - 5:
name_list = ["utkarsh", "rohan", "soham", "birjesh", "kamlesh", "suresh"]
name = input("Enter your name here: ")
if(name in name_list):
    print("Your name is already present in the name list")
else:
    print("Your username will be added soon")

# Question - 6:
'''
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
'''
marks = int(input("Enter marks here: "))

if(marks<=100 and marks>90):
    print("Your grade is: EX")
elif(marks<=90 and marks>80):
    print("Your grade is: A")
elif(marks<=80 and marks>70):
    print("Your grade is: B")
elif(marks<=70 and marks>60):
    print("Your grade is: C")
elif(marks<=60 and marks>50):
    print("Your grade is: D")
elif(marks<=50):
    print("Your grade is: F")

# Question - 7:
post = input("Enter your post here: ")
if("utkarsh" in post):
    print("This given post is talking about you")
else:
    print("The given post is talking about someone else")

# Chapter - 7: Practice set:
# Question - 1:
n = int(input("Enter number here: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

# Question - 2:
name_list = ["harry", "soham", "sachin", "rahul"]
for name in name_list:
    if(name.startswith("s")):
        print(f"Hello {name}")

# Question - 3:
n = int(input("Enter number: "))
i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i = i + 1

# Question - 4:
n = int(input("Enter a number: "))
for i in range(2, n):
    if(n%i==0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

# Question - 5:
n = int(input("Enter number here: "))
i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i = i + 1
print(sum)

# Question - 6:
n = int(input("Enter number here: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(product)

# Question - 7:
n = int(input("Enter number for pattern: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

# Question - 8:
n = int(input("Enter number for pattern: "))
for i in range(1, n+1):
    print("*" * i)

# Question - 9:
n = int(input("Enter number for pattern: "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")

# Question - 10:
n = int(input("Enter number here: "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n * (11-i)}")

# Chapter - 8: Practice set:
# Question - 1:
def greatest():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))

    if(num1>num2 and num1>num3):
        print(f"The greatest number is: {num1}")
    elif(num2>num1 and num2>num3):
        print(f"The greatest number is: {num2}")
    elif(num3>num1 and num3>num2):
        print(f"The greatest number is: {num3}")

greatest()

# Question - 2:
# f = 9/5*c+32
def c_to_f():

    c = int(input("Enter temp in c: "))
    f = (9/5*c)+32
    print(f"The temp in f are: {f}°F")

c_to_f()

# Question - 3:
a = "hello world 1"
b = "hello world 2"
c = "hello world 3"

print(a,end="")
print(b,end="")
print(c,end="")

# Question - 4:
'''
5 = 4 + 3 + 2 + 1
4 = 3 + 2 + 1
3 = natural_sum(n-1)
'''

def sum_of_natural_numbers(n):
    if(n==0):
        return 0
    return n + sum_of_natural_numbers(n-1)
n = int(input("Enter number for natural numbers are: "))
print(f"The sum_of_natural_numbers of the given number {n} is:",sum_of_natural_numbers(n))

# Question - 5:
def patter(n):
    if(n==0):
        return 0
    print("*" * n)
    patter(n-1)
n = int(input("Enter number here: "))
patter(n)

# Question - 6:
# cms = inches*2.54
def inches_to_cms():
    inches = int(input("Enter inches to convert into cms: "))
    cms = inches*2.54
    print(f"The inches into cms is: {cms}cm")
inches_to_cms()

# Question - 7:
def rem(l ,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["utkarsh", "rohan", "rahul", "suresh", "kamlesh", "utk"]
print(rem(l, "utk"))

# Question - 8:
def table():
    n = int(input("Enter number for table: "))
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")
table()

# Chapter - 9: Practice set:
# Question - 1:
with open("poem.txt") as f:
    data = f.read()

if("twinkle" in data):
    print("This file contain word twinkle")
else:
    print("No this file doesn't contain word twinkle")

# Question - 2:
import random

def game():
    print("The game is starting")
    score = random.randint(1, 100)
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"The score is: {score}")
    if(score>highscore):
        with open("highscore.txt", "w") as f:
            f.write(f"{str(score)}")
game()

# Question - 3:
def tables(n):
    tables  = ""
    for i in range(1, 11):
        tables += f"{n} X {i} = {n * i}\n"

    with open(f"Tables/table{n}.txt", "w") as f:
        f.write(str(tables))
    
for i in range(2, 21):
    tables(i)

# Question - 4:
with open("donkeyfile.txt") as f:
    data = f.read()

if("donkey" in data):
    new_data = data.replace("donkey","######")

with open("donkeyfile.txt", "w") as f:
    f.write(new_data)

# Question - 5:
words = ["donkey", "cow", "dog", "cat"]
with open("words.txt") as f:
    data = f.read()

for word in words:
    if(word in data):
        data = data.replace(word, "#"*len(word))
    
with open("words.txt", "w") as f:
    f.write(data)

# Question - 6:
with open("logfile.txt") as f:
    data = f.read()

if("python" in data):
    print("yes word python is presented in logfile.txt")
else:
    print("no word python is not presented in logfile.txt")

# Question - 7:
with open("logfile.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is presented in {lineno} line")
        break
    lineno = lineno + 1
else:
    print("no python is not presented in logfile.txt")

# Question - 8:
with open("this.txt") as f:
    data = f.read()

with open("copy_this.txt", "w") as f:
    f.write(f"{data}\nSee is have copied this file hahah noob")

# Question - 9:
with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    data1 = f1.read()
    data2 = f2.read()

if(data1 == data2):
    print("these both files are same")
else:
    print("these both files are different")

# Question - 10:
with open("file.txt", "w") as f:
    f.write("")

# Question - 11:
with open("renamefile.txt") as f:
    data = f.read()

with open("renamebypython.txt", "w") as f:
    f.write(data)

# Chapter - 10: Practice set:
# Question - 1:
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, salary: {self.salary}, Company: {self.company}")

pro1 = Programmer("utkarsh", 12000)
pro1.show_details()

pro2 = Programmer("rohan", 13000)
pro2.show_details()

pro3 = Programmer("rahul", 15000)
pro3.show_details()

pro4 = Programmer("suresh", 20000)
pro4.show_details()

pro5 = Programmer("kamlesh", 16000)
pro5.show_details()

# Question - 2:
class Calculator:
    def __init__(self, n):
        self.n= n

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n * self.n * self.n
calc1 = Calculator(5)
print("The squareroot of the given number is:",calc1.square())
print("The cuberoot of the given number is:",calc1.cube())

# Question - 3:
class Demo:
    a = 9

b = Demo()
b.a = 0
print(b.a)
print(Demo.a)

# Question - 4:
class Calculator:
    def __init__(self, n):
        self.n= n

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n * self.n * self.n
    
    @staticmethod
    def greet():
        print("Hello  user")
calc1 = Calculator(5)
calc1.greet()
print("The squareroot of the given number is:",calc1.square())
print("The cuberoot of the given number is:",calc1.cube())

# Question - 5:
# booking ticket, get status, get information
class Train:
    def __init__(self, trainno, ticket_price):
        self.trainno = trainno
        self.ticket_price = ticket_price

    def booking_ticket(self, fro, to):
        print(f"The ticket is booked in train number: {self.trainno} running from: {fro} to: {to}")
    
    def get_status(self):
        print(f"The train number: {self.trainno} is running on time")

    def get_fare(self, fro, to):
        print(f"The ticket price in train no: {self.trainno} running from {fro} to {to} is: {self.ticket_price}")

pass1 = Train(789456, 1230)
pass1.booking_ticket("Jaipur", "Japan")
pass1.get_status()
pass1.get_fare("Jaipur", "Japan")

# Question - 6:
class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(utkarsh):
        print(f"Name: {utkarsh.name}, Age: {utkarsh.age}")

d1 = Demo("utkarsh", 19)
d1.show()

d2 = Demo("rohan", 18)
d2.show()

# Chapter - 11: Practice set:
# Question - 1:
class Twodvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show_twodvector(self):
        print(f"The twodvector is: {self.i}i + {self.j}j")
    
class Threedvector(Twodvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show_threedvector(self):
        print(f"The threedvector is: {self.i}i + {self.j}j + {self.k}k")
    
v1 = Twodvector(1, 2)
v1.show_twodvector()
v2 = Threedvector(3, 4, 5)
v2.show_threedvector()

# Question - 2:
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Bhau Bhau")

dog1 = Dog()
dog1.bark()

dog2 = Dog()
dog2.bark()

dog3 = Dog()
dog3.bark()

# Question - 3:
class Employee:
    salary = 420
    increment = 12

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

a = Employee()
a.salaryafterincrement = 800
print(a.increment)

# Question - 4:
class Complex:
    def __init__(self, i, r):
        self.i = i
        self.r = r

    def __add__(self, c2):
        return Complex(self.i + c2.i, self.r + c2.r)

    def __str__(self):
        return f"{self.i}i + {self.r}r"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)

# Question - 5:
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, num):
        return Vector(self.i + num.i, self.j + num.j, self.k + num.k)
    
    def __mul__(self, num):
        return (self.i * num.i + self.j * num.j + self.k * num.k)

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

# Question - 6:
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, num):
        return Vector(self.i + num.i, self.j + num.j, self.k + num.k)
    
    def __mul__(self, num):
        return (self.i * num.i + self.j * num.j + self.k * num.k)

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

# Question - 7:
class Vector:
    def __init__(self, i):
        self.i = i

    def __len__(self):
        return len(self.i)
    
v1 = Vector([1, 2, 3])
print(len(v1))

# Chapter - 12: Practice set:
# Question - 1:
try:
    with open("file1.txt") as f:
        data = f.read()
except Exception as e:
    print(e)

try:
    with open("file2.txt") as f:
        content = f.read()
except Exception as e:
    print(e)

try:
    with open("file3.txt") as f:
        saman = f.read()
except Exception as e:
    print(e)

# Question - 2:
'''element number = 3,5,7
index number = 2,4,6'''
l = [1,2,3,4,5,6,7,8,9,0]
for index, item in enumerate(l):
    if(index == 2 or index == 4 or index == 6):
        print(item)

# Question - 3:
n = int(input("Enter number here: "))
table = [n*i for i in range(1, 11)]
print(table)

# Question - 4:
try:
    a = int(input("Enter number here: "))
    b = int(input("Enter number here: "))
except ZeroDivisionError as e:
    print("invalid input enter valid number")
else:
    print(f"The division of two numbers are: {a/b}")

# Question - 5:
with open("tables.txt", "a") as f:
    f.write(f"Table of {n}:{table}\n")

# Chapter - 13: Practice set:
# Question - 2:
name = input("Enter your name: ")
marks = int(input("Enter marks here: "))
phone_no = int(input("Enter phone number here: "))
detail = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_no)
print(detail)

# Question -3:
n = int(input('Enter number here: '))
l = [str(n*i) for i in range(1, 11)]
final =  "\n".join(l)
print(final)

# Question - 4: 
l = [45,78,12,56,23,0,4,156,18,0,15178]
def divisible_by_5(n):
    if(n%5==0):
        return True
    return False
final = filter(divisible_by_5, l)
print(list(final))

# Question - 5:
from functools import reduce
l = [1,2,3,4,5,6,7,8,9,0,12,45,78,89,56,23,0,15,48,78,851,126,65,61,1871,451,4208,8,1618,67,68,7,1268]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater, l))