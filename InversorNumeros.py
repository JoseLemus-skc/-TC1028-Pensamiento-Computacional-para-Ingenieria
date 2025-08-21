print('Ingrese el numero a invertir: ')
Num = float(input())

l=0
num=Num
n=0
x=0

while num>0:
    num = num//10
    l = l+1
    
while l>0:
    Num = Num/10
    x = (Num % 1)
    x = round(x,1)
    x = x * (10 ** l)
    n = n+x
    l = l-1
    Num = Num // 1
    
print('Numbero inverso: ',n)