#Figura anterior
print('Ingrese valores de la ficha anterior: ')
x = float(input())
y = float(input())

#Numero Figura Actual (contador)
c = 0

#Figura Virtual
n = 0 # numero superior
m = 0 # numero inferior

#Repetición de pasos para entrada (Figura anterior)
while x>n:
    c = c+1
    m = m+1
    if m == 6:
        n = n+1
        c = c+1
        m = n
while y>m:
    c = c+1
    m = m+1


print('Figura anterior:',n,'/',m,' Numero asociado: ',c)