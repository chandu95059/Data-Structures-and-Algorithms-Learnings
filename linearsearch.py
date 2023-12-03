arr=[1,8,9,99,100,150,120]
target = int(input("Enter Input: "))
flag = 0
for i in range(len(arr)):

    if arr[i] == target:
        print("element found at :",i)
        flag = 1 
if flag == 0:
    print("Element not found ")