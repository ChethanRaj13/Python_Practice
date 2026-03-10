# store in an distionary

dist = {}
print(dist)

dist.update({"table" : ["a piece of furniture", "list of facts and figure"],
             "cat" : "a small animal"})

print(dist)

#-----------------------------------------------------------------

# your given list subjects assume 1 subject in 1 classroom how many classrooms are required 

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print(len(subjects))

#-----------------------------------------------------------------

# WAP marks of 3 subjects from the user and store them in the dictionary 
# start with empty dictionary and add marks. Use subject name as key and marks as value
 
marks = {}

eng = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))

marks.update({"English" : eng, "Maths" : maths, "Science" : science})
print(marks)

