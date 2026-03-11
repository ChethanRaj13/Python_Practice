# WAP to print the length of the list (using list as parameter)

def length(list):
    i = 0
    for el in list:
        i += 1
    return i

list = [1,2,3,4,5,6,7,8,9,10]
length_list = length(list)
print(length_list)

#--------------------------------------------------------------

# WAP to print all the elements in one line (using list as paramenter)

def print_list(list):
    for el in list:
        print(el, end = " ")

list = [1,2,3,4,5,6,7,8,9,10]
print_list(list) 

#--------------------------------------------------------------

# WAP to find the factorials of n

def fact(n):
    num = 1
    for i in range(1, n+1):
        print(i * num)
        num *= i 

n = int(input("Enter the number: "))
fact(n)

#--------------------------------------------------------------

# WAP to convert USD to INR

def usd_inr(amt):
    return (92.16 * amt)

amt = float(input("Enter the amount in USD: "))
inr_amt = usd_inr(amt)
print(inr_amt)

#--------------------------------------------------------------

# WAP to recursively calculate the sum of n numbers

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the number: "))

res = sum(n)
print(res)

#--------------------------------------------------------------

# WAP to recurssively print the list of elements

def print_list(list, n):
    if(n == len(list)):
        return
    print(list[n])
    print_list(list,n+1)

list = [1,2,3,4,5,6,7,8,9,10]

print_list(list, 0)