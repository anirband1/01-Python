# Run 2 modes of the program. Ask input for the mode to be run. 
# a. Use marks-test.txt for test mode (T)
# b. Use marks.txt for run mode (R)
#
# 1. How many students are there in the class
# 2. Average of all the marks across the year
# 3. Who got the highest marks. Give shabashi to him/her
# 4. Who got the lowest marks. Give bashing to him/her
# 5. Average of all marks per student

# average function. can also be used just as mean(lst)
def avg(lst):
    return sum(lst) / len(lst) 

# Main Program
total = 0
item = 0
maxMark = 0
minMark = -1
classDict = dict()

option = input("Enter mode (T)est/(R)un: ")
if option == 'T':
    file1 = open('../Data/marks-test.txt')
elif option == 'R':
    file1 = open('../Data/marks.txt')
else:
    print("Not a valid option pah!")
    exit()

line1 = file1.readline()
while(line1 != ""):
    list1 = line1.split(':')
    name = list1[0]
    mark = list1[1]

    if int(mark) > int(maxMark):
        maxName = name
        maxMark = int(mark)   
    if int(minMark) == -1 or int(mark) < int(minMark):
        minName = name
        minMark = int(mark)    

    total = total + int(mark)
    item += 1

    if not (name in classDict):
        classDict[name] = list()
    classDict[name].append(int(mark))
    
    line1 = file1.readline()

print("\nNumber of students is ",len(classDict))
print("\nAverage of all the marks is ",round(total/item, 2),"\n")
print (maxName, "got the highest marks with", maxMark, "so here is a SHABASH CHHOTE!")
print (minName, "got the lowest marks with", minMark, "so here is a DHISHOOOM!!!\n")
for key in classDict:
    print (key, ":", classDict[key], " with average of ", round(avg(classDict[key]),2))
