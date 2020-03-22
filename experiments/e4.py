# Run 2 modes of the program. Ask input for the mode to be run. 
# a. Use marks-test.txt for test mode (T)
# b. Use marks.txt for run mode (R)
#
# 1. How many students are there in the class
# 2. Average of all the marks across the year
# 3. Who got the highest marks. Give shabashi to him/her
# 4. Who got the lowest marks. Give bashing to him/her
# 5. Average of all marks per person

# average of the whole year

total = 0
item = 0
file1 = open('../Data/marks-test.txt')
file2 = open('../Data/marks-test.txt')
line1 = file1.readline()
line2 = file2.readline()
while(line1 != ""):
    list1 = line1.split(':')
    name = list1[0]
    mark = list1[1]
    total = total + int(mark)
    item += 1
    line1 = file1.readline()
    line1 = line1.rstrip()

print(" \nAverage of the whole year is",total/item,"\n")

# highest marks

count = 1
maxVal=0
minVal=1000000
minname = ''
maxname = ''
list2 = {}

while (count <= item):
    list2 = line2.split(':')
    mark1 = list2[-1]
    name1 = list2[0]
    list2 = {mark1 :name1}
    if eval(mark1) >= int(maxVal):
        maxname = name1
        maxVal = int(mark1)   
    if eval(mark1) <= int(minVal):
        minname = name1
        minVal = int(mark1)    
    line2 = file2.readline()
    count+=1

print (maxname,"got the highest marks with",maxVal)
print ("SHABASH CHHOTE\n")
print ("and\n") 
print (minname,"got the lowest marks with",minVal)
print ("<punch>\n")
