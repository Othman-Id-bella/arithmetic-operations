A=float(input("enter nomber A:"))
B=float(input("enter nomber B:"))
op=input("enter the operation:")

if op=="+" :
    print("A+B=",A+B)
elif op=="-" :
    print("A-B=",A-B)
elif op=="*" :
    print("A*B=",A*B)
elif op=="/" :
    if B!=0:
        print("A/B=",A/B)
    else:
        print("division by 0 is impossible.")
else:
    print("the operation is not correct.")