#find all comination where a+b+c = 0

array = [-1,0,1,2,-1,-4,3]

new_array = []
for i in range(len(array)):
    for j in range(i+1,len(array)-1):
        if (array[i]+array[j]+array[j+1]) == 0:
            new_array.append([array[i],array[j],array[j+1]])
        
print(new_array)
