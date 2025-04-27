
t=int(input("enter the number of test cases:"))
list=[]
for i in range(t):
    list.append(int(input("enter the number:")))

for i in list:
    num,q,count=i,0,0
    while num!=0:
        q=num%10
        if q==0:
            pass
        else:
            if i%q==0:
                count+=1
        num//=10
    print(count)



                







