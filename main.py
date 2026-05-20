# ================header===============
name=input("Enter the name")
age=int(input("Enter the age"))
Email=input("Enter the email_id ")
print(name)
print(age)
print(Email)
# =================First logic ====================
bal = 10000
if age>=18:
    print("you can access the ATM machine")
    print("1.Checkbalance")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Exit")

    choice=int(input("Enter the choice"))
    match choice:
        case 1:
            print("Your balance is: "+bal)
        case 2:
            print("Enter your deposit amount:")
            Dp=int(input())
            bal+=Dp
            print(bal)
        case 3:
            print("Enter your Withdrawal Amount:")
else:
    print("you cannot access the ATM machine")