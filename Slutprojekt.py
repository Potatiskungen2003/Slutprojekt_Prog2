
from getpwd import getpwd

""" I admin classen vill du ha alla metoder som ska gå att använda
I aludt har du några färre typ att kolla andras lösenor eller liknande 
I minor ska man nästan inte ha några ärvda metoder förutom dem som visar saker """
class Bank:
    def __init__(self, name, password, balance):
        self.name = name
        self.__password = password
        self.balance = balance
    
    def login():
        user_name = input(str("Username:"))
        user_password = input(str("Password:"))
        if user_name == 
        

class Admin(Bank):
    pass

class Adult(Bank):
    pass

class Minor(Bank):
    pass


anvandare = Bank('jeff', 'jeeeeeef', '34567890')

print(anvandare.__password)

secret = getpwd()

print(secret)
