#Banking Program

ankna_total_balance=0
shilpa_total_balance=0
Pijush_total_balance=0
Budhyadeb_total_balance=0
nayan_total_balance=0

def saw_bank_balence(total_balance):
    print(f"Now your balance is ${total_balance:.2f}")
def deposit(total_balance):
    amount=float(input("Enter the amount for deposit="))
    if(amount<=0):
        print("Sorry,It is not a valid amount.\nPlease retry and enter a valid amount")
        return 0
    else:
        return amount


def withdraw(total_balance):
    amount=float(input("Enter your amount for withdrawal="))
    if(amount<=0):
        return 0
    elif(total_balance<amount):
        print("You have not enough cash.\nPlease retry and enter a valid amount")
        return 0
    else:
        return amount
    


def open(balance):
    total_balance=balance
    is_atm_entered=True
    while(is_atm_entered==True):
        print("Enter 1 for see your bank balance")
        print("Enter 2 for deposit money")
        print("Enter 3 for withdraw money")
        print("Enter 4 for exit")
        key=int(input("Enter your choice="))
        if(key==1):
            saw_bank_balence(total_balance)
        elif(key==2):
            total_balance += deposit(total_balance)
        elif(key==3):
            total_balance -= withdraw(total_balance)
        elif(key==4):
            print("Thank You,You are exited")
            is_atm_entered=False
        else:
             print("Please enter a valid input")
    return(total_balance)


def ankan_koley():
    global ankna_total_balance
    nowbalance=open(ankna_total_balance)
    ankna_total_balance=nowbalance


def shilpa_koley():
    global shilpa_total_balance
    nowbalance=open(shilpa_total_balance)
    shilpa_total_balance=nowbalance 


def pijush():
    global Pijush_total_balance
    nowbalance=open(Pijush_total_balance)
    Pijush_total_balance=nowbalance 


def budhyadeb():
    global Budhyadeb_total_balance
    nowbalance=open(Budhyadeb_total_balance)
    Budhyadeb_total_balance=nowbalance


def nayan(): 
    global nayan_total_balance
    nowbalance=open(nayan_total_balance)
    nayan_total_balancee=nowbalance


#check the time


import time
nowTime=time.strftime("%H:%M:%S")
print("Now the time is=:",nowTime)
hour=int(time.strftime("%H"))
if(hour>=9 and hour<=17):
    print("Bank is open")
    if_accunt=True
    while(if_accunt==True):

        #check the accunt number
        
        accunt=int(input("Enter your account number="))
        if(accunt==909196): 
            password=909196
            print("It is Mr.Ankan Koley's account")
            accuntpass=int(input("Enter your password="))
            if(accuntpass==password):
               print("Your account is opened")
               ankan_koley()
            else:
                print("Wrong Password")             
        elif(accunt==909195):
            password=909195
            print("It is Mrs.Shilpa Koley's account")
            accuntpass=int(input("Enter your password="))
            if(accuntpass==password):
                print("Your account is opened")
                shilpa_koley()
            else:
                print("Wrong Password")
        elif(accunt==909194):
            password=909194
            print("It is Mr.pijush's account")
            accuntpass=int(input("Enter your password="))
            if(accuntpass==password):
                print("Your account is opened")
                pijush()
            else:
                print("Wrong Password")
        elif(accunt==909193):
            password=909193
            print("It is Mr.Budhyadeb's account")
            accuntpass=int(input("Enter your password="))
            if(accuntpass==password):
                print("Your account is opened")
                budhyadeb()
            else:
                print("Wrong Password")
        elif(accunt==909192):
            password=909192
            print("It is Mr.Nayan's account")
            accuntpass=int(input("Enter your pasword="))
            if(accuntpass==password):
                print("Your account is opened")
                nayan()
            else:
                print("Wrong Password")
        else:
            print("Please enter a valid account number")
else:
    print("Bank is closed")