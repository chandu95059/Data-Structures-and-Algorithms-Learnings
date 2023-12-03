arr=[1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
target = int(input("Enter target number:"))

left = 0
right = len(arr)-1
flag = 0
while(left<=right):
    mid = (left+right)//2
    if arr[mid]==target:
        print("Element found at ",mid)
        flag = 1
        break
    elif arr[mid]<target:
        left = mid + 1
    else:
        right = mid - 1
if flag == 0:
    print("Element not found ")
        
            