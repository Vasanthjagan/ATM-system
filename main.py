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
    match bal:
        case 1:
            print("Your balance is: "+bal)
            
else: 
    print("you cannot access the ATM machine")
    