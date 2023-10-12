from calculator import add,mul,div,sub
import __init__
#all def main  will be same 
def main():
    print("calculator package")
    print("select operation")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")

    choice=int(input("please enter the operation you want to run 1/2/3/4 : "))

    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))

    if choice==1:
        result= add(num1,num2)
        print("Addition is ",result)
    
    if choice==2:
        result= sub(num1,num2)
        print("Substraction is ",result)

    if choice==3:
        result= mul(num1,num2)
        print("Multiplication is ",result)    

    if choice==4:
        result= div(num1,num2)
        print("Division is ",result)

if __name__=="__main__":
    main()
