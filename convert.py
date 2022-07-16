        
R = input()
longness = len(R)

for k in R:
    if k!='0' and k!='1':
        print('Error number')
        raise SystemExit  
num=0
for i in range(len(R)):
    k1=int(R[i])
    num = num+k1*(2**(len(R)-i-1))
    
print(num)

