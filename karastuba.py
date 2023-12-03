x=input()
y=input()
m=max(len(x),len(y))
#padding of zero's
if(m%2!=0):
    m+=1
    x+='0'*(m-len(x))
    y+='0'*(m-len(y))
else:
    x+='0'*(m-len(x))
    y+='0'*(m-len(y))
mid = m//2
xh=x[:mid]
xl=x[mid:]
yh=y[:mid]
yl=y[mid:]

#step-1 : xh*yh
s1 = int(xh)*int(yh)
#step-2 : xh*yh
s2 = int(xl)*int(yl)
#step- 3 : (xh+xl)*(yh+yl)
s3 = (int(xh)+int(xl))*(int(yh)+int(yl))

result = s1*(10**m)+(s3-s1-s2)*(10**(m//2))+s2
print(result)