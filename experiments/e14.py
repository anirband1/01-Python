#initialize

file1 = open("../Data/num2.txt")
num_of_odd = 0
num_of_even = 0
mode = 0
array = []
line = file1.readline()



#assigning the values

while (line!="") :
    nline = int(line)
    if nline % 2 == 0:
        num_of_even += 1
        array.append(nline)
    elif nline % 2 == 1:
        num_of_odd += 1
        array.append(nline)
    line = file1.readline()

#sorting array

array.sort()

 #main logic 

#median
if len(array)%2 == 0:
    print("median of numbers is",array[int(len(array)/2)])
elif len(array)%2 == 1:
    print("median of numbers is",array[int((len(array)+1)/2)])

#mode

for occurence in array:
    if array.count(occurence) > mode:
        mode = occurence

print("mean of numbers is ",sum(array)/len(array))
print("number of even numbers is ",num_of_odd)
print("number of even numbers is ",num_of_even)
print("number of numbers is ", len(array) )
print("largest value is ",max(array))
print("least value is ",min(array))
print("mode of numbers is ",mode)
