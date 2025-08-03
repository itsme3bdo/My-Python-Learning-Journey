from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
diic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate():
    num1 = int(input("Enter the 1st number"))
    oper = input('Enter the operator of choice, "+", "-", "*" or "/"')
    num2 = int(input("Enter the 2nd number"))
    for key in diic:
        if key == oper:
            ans = diic[key](num1, num2)
            print(ans)
    again = input('Do you want to continue with the previous result, write "y" for yes and "n" for no\n').lower()
    return ans,again

continued=True
ans=None
while continued:
    # num1=int(input("Enter the 1st number\n"))
    # oper=input('Enter the operator of choice, "+", "-", "*" or "/"\n')
    # num2 = int(input("Enter the 2nd number\n"))
    # for key in diic:
    #     if key == oper:
    #         ans= diic[key](num1,num2)
    #         print(ans)
    ans, again = calculate()
    # again=input('Do you want to continue with the previous result, write "y" for yes and "n" for no\n').lower()
    while again == "y":
        num1 = ans
        oper = input('Enter the operator of choice, "+", "-", "*" or "/"\n')
        num2 = int(input("Enter the 2nd number\n"))
        for key in diic:
            if key == oper:
                ans = diic[key](num1, num2)
                print(ans)
        again = input('Do you want to continue with the previous result, write "y" for yes and "n" for no\n').lower()

    else:
        # num1=int(input("Enter the 1st number\n"))
        # oper=input('Enter the operator of choice, "+", "-", "*" or "/"\n')
        # num2 = int(input("Enter the 2nd number\n"))
        # for key in diic:
        #     if key == oper:
        #         ans= diic[key](num1,num2)
        #         print(ans)
        calculate()
