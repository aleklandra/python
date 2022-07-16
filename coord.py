import math

def is_number(tmp :list):
    try:
        list(map(int, tmp))
        return True
    except ValueError:
        return False
        
def long(tmp :list):
    if len(tmp)!=2:
        print("Need 2 coordinates")
        return False
    else:
        return True
        
def distanse(tmp1 :list, tmp2 :list):
    return math.sqrt((tmp1[0] - tmp2[0])*(tmp1[0] - tmp2[0]) + (tmp1[1] - tmp2[1])*(tmp1[1] - tmp2[1]))

point1 = list(input().split())
point2 = list(input().split())
point3 = list(input().split())

if long(point1)==False or long(point2)==False or long(point3)==False:
    raise SystemExit

if is_number(point1) == False or is_number(point2)== False or is_number(point3)== False:
    print("You should put only integer numbers")
    raise SystemExit
else:
    temp_num1=list(map(float, point1))
    temp_num2=list(map(float, point2))
    temp_num3=list(map(float, point3))

if max(temp_num1)>50 or max(temp_num2)>50 or max(temp_num3)>50 or min(temp_num1)==0 or min(temp_num2)==0 or min(temp_num3)==0:
    print("You should put only numbers from 1 to 50")
    raise SystemExit


dist = []
dist.append(distanse(temp_num1, temp_num2))
dist.append(distanse(temp_num1, temp_num3))
dist.append(distanse(temp_num2, temp_num3))

dist_min = round(min(dist),2)

print(format(dist_min,'.2f'))
