# Create student class that takes name and marks of 3 subject as arguments in constructor.
# create a methord to find the average

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def get_avg(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3.0
        return avg


s1 = Student("raj",91,99,100)
print(s1.get_avg())

#-----------------------------------------------------------------------

# Create Account class with 2 attributes - balance and acc no
# create a methord for debit and credit and print balance

class Bank:

    def __init__(self, accno, bal):
        self.accno = accno
        self.bal = bal
    
    def debit(self, amt):
        if amt > self.bal:
            print("insafficient balance")
        else:
            self.bal -= amt
            print(amt,"got debited, balance:",self.bal)
    
    def credit(self, amt):
        self.bal += amt
        print(amt,"successfully credited, balance:", self.bal)
    
    def check_bal(self):
        print("balance:",self.bal)

a1 = Bank("12345", 10000)
a1.debit(111111)
a1.debit(100)
a1.credit(1000)
a1.check_bal()
