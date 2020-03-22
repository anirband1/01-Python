lst = [2,6,6,5,7,2,-4,4,-3,4,5,20,-4,0,6,5,4,5,6,5,20,42,-3,3,4,1,-3]
n=len(lst) - 1      # delete from end
print("original -  ",lst)
lst.sort()
while n >= 1:
    #print(lst,n,lst[n],lst[n-1])
    if lst[n] == lst[n-1]:
        lst.remove(lst[n])
    n-=1
print("final - ",lst)