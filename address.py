"""Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры K1, а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру K2, которая расположена в подъезда P2 на этаже N2. Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычилсяет номер подъезда P1 и номер этажа N1 квартиры K1."""



def is_number(tmp :list):
    try:
        list(map(int, tmp))
        return True
    except ValueError:
        return False

def division (num1 :int, num2 :int) -> list:
    if num1%num2 == 0:
        return [0, num1//num2]
    else:
        return [1, (num1//num2)+1]     
temp = list(input().split())

if is_number(temp) == False:
    print("You should put only integer numbers")
    raise SystemExit
else:
    temp_num=list(map(int, temp))

if len(temp_num)<5:
    print("You should write 5 numbers!")
    raise SystemExit
    
if max(temp_num)>1000000:
    print("Numbers should be less than 10^6")
    raise SystemExit
elif min(temp_num)<=0:
    print("Numbers should be grater than 0")
    raise SystemExit
    
    
#x - кол-во квартир на этаж
#x = K2/((P2-1)*M+N2)
#P1 = division(K1, x*M)
#N1 = division(K1-(P1-1)*x*M,x)
#temp_num[0]=K1, temp_num[1]=M, temp_num[2]=K2, temp_num[3]=P2, temp_num[4]=N2

if temp_num[0]==temp_num[2]:
    print(temp_num[3], temp_num[4])
else: 
    x = temp_num[2]/((temp_num[3]-1)*temp_num[1]+temp_num[4])
    if x<1:
        print("-1 -1")
    else:
        list_x=division(temp_num[2],(temp_num[3]-1)*temp_num[1]+temp_num[4])
        list_p1 = division(temp_num[0], list_x[1]*temp_num[1])
        list_n1 = division(temp_num[0]-((list_p1[1]-1)*list_x[1]*temp_num[1]),list_x[1])
        if list_x[0]==0 and temp_num[3]==1:
            list_p1[1]=0
            print(list_p1[1], list_n1[1])
        else:
            print(list_p1[1], list_n1[1])


