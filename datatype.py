#Number 

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


#Interger DataType
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float DataType
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


#complex datatype

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))




x = 1    
y = 2.8  
z = 1j  

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



#Random
import random

print(random.randrange(1, 10))

#String datatype
a = "Hello"
print(a)

#Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#String Length
a = "Hello, World!"
print(len(a))


#Check The String
txt = "The best things in life are free!"
print("free" in txt)

#Upper Case
a = "Hello, World!"
print(a.upper())


#Lower Case
a = "Hello, World!"
print(a.lower())


#Remove White Space 
a = " Hello, World! "
print(a.strip())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split  The String
a = "Hello, World!"
b = a.split(",")
print(b)

#Concatination
a = "Hello"
b = "World"
c = a + b
print(c)

#Boolean Datatype
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Evaluate Values And Variable
print(bool("Hello"))
print(bool(15))




#Functions Can Return The Value
def myFunction() :
      return True

print(myFunction())


#List Data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


#Type()
mylist = ["apple", "banana", "cherry"]

print(type(mylist))

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#change Item VAlue
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

#Change Of Item Value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

#Insert Values
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 


#Add The Value  with append() method
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

#Removed Speciefy Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#TUple Item Datatype
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


#Set

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
























