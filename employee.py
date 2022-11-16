tax=0
net=0
namel=[]
regl=[]
sall=[]
taxl=[]
while(True):
    n=input("enter the number of employees:")
    if(n.isdigit()):
        n=int(n)
        break;
    else:
        print("enter the valid input")
for i in range(1,n+1,1):
    print("employee",i)
    while(True):
        name=input("enter the name of the employee:")
        if(name.isalpha()):
            namel.append(name)
            break;
        else:
            print("enter the valid input")
    while(True):
        reg=input("enter the employee id:")
        if(reg.isalnum()):
            regl.append(reg)
            break;
        else:
            print("enter the valid input")
    while(True):
        sal=input("entet the salary of employee:")
        if(sal.isdigit()):
            sal=int(sal)
            sall.append(sal)
            tax=sal*0.1
            taxl.append(tax)
            net=sal-tax
            break;
        else:
            print("enter tge valid input")
print("Name:",end="     ")
for j in range(1,n+1,1):
    print(namel[j-1],end="    ")
print("")
print("Reg No.:",end="  ")
for k in range(1,n+1,1):
    print(regl[k-1],end="    ")
print("")
print("Salary:",end="   ")
for l in range(1,n+1,1):
    print(sall[l-1],end="    ")
print("")
print("tax:",end="    ")
for m in range(1,n+1,1):
    print(tax[m-1],end="    ")
print("")


    
        
