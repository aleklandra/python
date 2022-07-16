

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
 
R = input()       
if is_number(R) == False:
    print('All numbers must be integer')
    raise SystemExit
R1=float(R)

V = (4*R1*R1*R1*3.14)/3

print(format((round(V,2)),'.2f'))
