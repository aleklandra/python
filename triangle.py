"""Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой."""

sides = []

for k in range(3):
    a = int(input())
    if a<=0:
        print('Error')
        raise SystemExit
    sides.append(a)

if len(sides) == 0:
    print('Error')
    raise SystemExit

ind = 0    
for k in range(2):
    if sides[k]>sides[k+1]:
        ind = sides[k]
        sides[k]=sides[k+1]
        sides[k+1]=ind
        
if sides[0]+sides[1]>sides[2]:
    print('YES')
else:
    print('NO')
