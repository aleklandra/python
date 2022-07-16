"""Решите в целых числах уравнение:
sqrt(ax+b)=c
a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет."""


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
        
a = input()
b = input()
c = input()

if is_number(a) == False or is_number(b) == False or is_number(c) == False:
    print('All numbers must be integer')
    raise SystemExit

a=float(a)
b=float(b)
c=float(c)

if a%1!=0 or b%1!=0 or c%1!=0:
    print('All numbers must be integer')
    raise SystemExit


if c<0:
    print('NO SOLUTION')
elif a==0 and b==c*c:
    print('MANY SOLUTIONS')
elif a==0 and b!=c*c:
    print('NO SOLUTION')
elif (c*c-b)%a != 0:
    print('NO SOLUTION')
else:
    print(int((c*c-b)/a))


