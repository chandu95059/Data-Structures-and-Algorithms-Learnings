heystack = 'abczyzxyzxyz'
needle = 'xyz'

for i in range((len(heystack)-len(needle))+1):
    flag = 0
    for j in range(len(needle)):
        if heystack[i+j]==needle[j]:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print("match found at index:",i)
if flag == 0:
    print("Pattern Not Found")