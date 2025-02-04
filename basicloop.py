x = 0
for x in range(1,10):
    if x%2==0:
        print(x)
        x+=1
    elif x%2!=0:
        print(x,"Không chia hết cho 2")   
    else:
        print("check")