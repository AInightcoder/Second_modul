arr = [2,5,8,9,10,5,6,4,47]
arr1=[]
for x in range(0, len(arr),2):
   arr1.append(arr[x])
arr.extend(arr1)
print(arr)