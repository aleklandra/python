from decimal import Decimal

def is_number(str):
    try:
        Decimal(str)
        return True
    except ValueError:
        return False
        
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a        
    return a

num = input()

if is_number(num) == False:
    print('You should wright only numbers')
    raise SystemExit
num1 = Decimal(num)

if Decimal(round(num1,0)) == num1:
    print(format(round(num1,0),'.0f'))
    
else:
    ind = 1
    num2 = num1
    while num2!=int(num2):
        num2 = num2*10
        ind = ind*10
        
    de = gcd(num2, ind)
    a = int(num2/de)
    b = int(ind/de)
    print(a,'/',b)

