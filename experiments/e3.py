file1 = open("../Data/num.txt")
l=[]
l=file1.readline()
num=0
arrno=0
it=0
while(l!=""):
    num = num + int(l)
    it+=1
    l=file1.readline() 
print(num/it)
