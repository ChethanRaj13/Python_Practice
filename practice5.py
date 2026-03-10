# WAP to print 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1 

#-------------------------------------------------------------

#WAP to print 100 to 1

i = 100
while i > 0:
    print(i)
    i -= 1

#-------------------------------------------------------------

# WAP to print multiple of table

num = int(input("Enter the number: "))

i = 1

while i <= 10:
    print(num * i)
    i += 1

#-------------------------------------------------------------

# WAP to print all the elements of list 

list = [1,2,3,4,5,6,7,8,9,10]

i = 0
while i < len(list):
    print(list[i])
    i += 1

#-------------------------------------------------------------

# linear search

list = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Enter the number to search: "))

i = 0
while i < len(list) and list[i] != num:
    i+=1

if i == len(list):
    print("not found")
else:
    print("found")    

#-------------------------------------------------------------

# WAP to print all the element in the list

list = [1,2,3,4,5,6,7,8,9,10]

for el in list:
    print(el)

#-------------------------------------------------------------

# WAP to linear search using for loop

list = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Enter the number: "))

for el in list:
    if(num == el):
        print("Element was found")
        break
else:
    print("Element was not found")

#-------------------------------------------------------------

# WAP to print 1 to 100 using range

for i in range(1,101,1):
    print(i)

#-------------------------------------------------------------

# WAP to print 100 to 1 using range

for i in range(100, 0, -1):
    print(i)

#-------------------------------------------------------------

# WAP to print multiple of a number

num = int(input("Enter the number: "))

for i in range(11):
    print(num * i)

#-------------------------------------------------------------

# WAP to find the sum of n numbers 

num = int(input("Enter the number: "))

sum = 0

for i in range(num+1):
    sum += i

print(sum)

#-------------------------------------------------------------

# WAP to find the factorial of n numbers 

num = int(input("Enter the number: "))

mul = 1
i = 1

while i <= num:
    mul *= i
    i += 1

print(mul) 