
from getpwd import getpwd
import openpyxl
import time

""" I admin classen vill du ha alla metoder som ska gå att använda
I aludt har du några färre typ att kolla andras lösenor eller liknande 
I minor ska man nästan inte ha några ärvda metoder förutom dem som visar saker """
class Bank:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

    def __str__(self):
        return f"Namn: {self.name}\nSaldo: {self.balance} kr"
    
    def account_balance(self):
        return f"Ditt saldo är: {self.balance} kr"

    def change_password(self):
        pass

    def save_data(self):
        path = "Bank_info.xlsx"
        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active
        max_ro = sheet_obj.max_row

        for x in range(1, max_ro + 1):

            name = sheet_obj.cell(row = x, column = 1)
            print(name.value)
            if name.value == self.name:

                cell_obj = sheet_obj.cell(row = x, column = 1)
                cell_obj.value = "funkar"
                print(cell_obj.value)
                break # Saker inte funka som det ska

class Admin(Bank):
    def __init__(self, name, password, balance):
        super().__init__(name, password, balance)

class Adult(Bank):
    def __init__(self, name, password, balance):
        super().__init__(name, password, balance)

class Minor(Bank):
    def __init__(self, name, password, balance):
        super().__init__(name, password, balance)

    def change_password(self):
        print("Fråga dina päron")

# Functions
def login():
    path = "Bank_info.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    max_ro = sheet_obj.max_row

# rita i X-L sak
# cell_obj = sheet_obj.cell(row = x, column = i)
# cell_obj.value = "vad du vil ändra det till"

# square = sheet_obj["a1"]
# square.value = "något bra"

###########################################################
# Visar bara lösenord och sånt. Ej relevant för programmet. 
    for x in range(1, max_ro + 1):
        for i in range(1, max_col + 1):

            cell_obj = sheet_obj.cell(row = x, column = i)
            
            print(cell_obj.value, end=' ')
        print()
###########################################################
    trys = 4
    run = True
    while run == True:
        
        input_name = str(input("Username: "))
        password = getpwd()

        for x in range(1, max_ro + 1):

            name = sheet_obj.cell(row = x, column = 1)
            
            pass_check = sheet_obj.cell(row = x, column = 2)

            if password == pass_check.value:
                if name.value == input_name:
                    print("Du hade rätt användarnamn och lösenord")
                    run = False
                    break

        if password != pass_check.value or name.value != input_name:
                trys = trys-1
                print("Fel användarnamn eller lösenord")
                print("Du har", trys, "försök kvar")
                if trys < 1:
                    print("Du kan logga i igen om:")
                    for i in range(6):
                        print(f"{(6-i)*10} sekunder")
                        time.sleep(1)
                    trys = 4


    role = sheet_obj.cell(row = x, column = 4)
    balance = sheet_obj.cell(row = x, column = 3)
    if role.value == "Admin":
        user = Admin(name.value, pass_check.value, balance.value)
    
    elif role.value == "Adult":
        user = Adult(name.value, pass_check.value, balance.value)
    
    elif role.value == "Minor":
        user = Minor(name.value, pass_check.value, balance.value)
    
    print(user)
    return user

def main():
    user = login()
    loginacces = True
    while loginacces == True:
        print("\nVad vill du göra?"
            "\n(1) - Saldo\n(2) - Min profil"
            "\n(3) - Byt användare"
            "\n(4) - Logga ut och avsluta")
        try:
            user_input = int(input("Nr:"))
        except:
            print("Använd hela/siffror")

        if user_input == 1:
            print(user.account_balance())# Hämta saldo
        elif user_input == 2:
            print()# Gå till profil
        elif user_input == 3:
            print()# Byta användare
        elif user_input == 4:
            return(user.save_data())# Avsluta och spara data
        
main()