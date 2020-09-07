#任意10进制数转换为任意进制数
def cal(m,n):
    s=""
    while m>=n:
        s=str(m%n)+","+s
        m=m//n
    return (str(m)+","+s)[:-1]
#print(cal(188,2))

#任意进制数转换为10进制数
def sal(n=8,m=""):
    s=0
    m=m.split(",")
    for i in range(len(m)):
        s=eval(m[i])*n**(len(m)-i-1)+s
    return s
#print(sal(9,"2,2,8"))

#进制n1的数m转换为进制n2的数
def slc(n1,m,n2):
    return cal(sal(n1,m),n2)

#TODO:密码学？
print("1.1,0.12")
print(slc(1.2,"1.1,0.12",10))
print(slc(10,"1.1,0.12",1.2))

print(slc(10,"1.44",1.2))
print(slc(1.2,"1.0,0.24",10))
print(slc(10,"1.0,0.24",1.2))
