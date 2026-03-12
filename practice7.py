# WAP to create a file and add some data

file = open("sample.txt", "w")

file.write("hi everyone\nwe are learing file I/O\nusing java\ni like programming in java")
file.close()

#-----------------------------------------------------------------

# WAP to replace java with python in sample.txt

with open("sample.txt","r") as f:
    data = f.read()
    
data1 = data.replace("java", "python")

with open("sample.txt","w") as f:
    f.write(data1)

#-----------------------------------------------------------------

# WAP to search if the word "learing" exists in the file or not

with open("sample.txt","r") as f:
    data = f.read()

if "learing" in data:
    print("TRUE")
else:
    print("FLASE")

#-----------------------------------------------------------------

# WAP to find in which line of the file does the word "learing" occur first.
# print -1 if word not found

# with open("sample.txt","r") as f:

    count = 1
    data = True
    while data:
        data = f.readline()
        if("learning" in data):
            print(count)
            break
        count += 1
    else:
        print(-1)

#-----------------------------------------------------------------

# find the even numbers separated by commma and print them

with open("sample2.txt","r") as f:
    data = f.read()
    list = data.split(",")
    for num in list:
        if(int(num) % 2 == 0):
            print(num) 