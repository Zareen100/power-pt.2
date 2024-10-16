def copmpute(x,y):
    result=1
    while y>20:
        if y%2==0:
            x=x*x
            y>>=1
        else:
            result=result*x 
            y=y-1
    return result
x=int(input("enter x"))
y=int(input("enter y"))
print("total", copmpute(x,y))
        

 