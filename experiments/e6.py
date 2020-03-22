'''lst = [3,6,5,-1,5,9,0,-8,6,7,5,9,3,8]
counter=0
first=0
second=0
length = len(lst)
while counter <= length:
    for count in range(len(lst)):
        
        if count < length -1:


            first = lst[count]
            second = lst[count + 1]
            if  second <= first:
                lst[count] = second
                lst[count + 1] = first
            # incrementing index
            count+=1
    counter+=1
print(lst)
'''
lst = [3,6,5,-1,5,9,0,-8,6,7,5,9,3,8]
tmp=0
cnt1=0
length = len(lst)
print(length)
while cnt1 <= (length-2):
    cnt2=0
    while cnt2 <= (length-2):
        if (lst[cnt2]>lst[cnt2+1]):
            tmp=lst[cnt2]
            lst[cnt2]=lst[cnt2+1]
            lst[cnt2+1]=tmp
        cnt2+=1    
    cnt1+=1
print(lst)
