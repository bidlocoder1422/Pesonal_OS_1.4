import os
from ClassAuntef import *
import datetime
from current_loc import *
class Menu:
    """different menu
       using for access for applications or options
    """
    def __init__(self, lvl):
        self.lvl = lvl
        self.current_location=location.return_city()
    def prinmaintmenu(self, username):
        now = datetime.datetime.now()
        os.system('cls')
        print(now.strftime("%d.%m.%Y %I:%M %p"))  # форматируем дату)
        print('Logged as: ',username,'\t\t\t\t','Location: ',self.current_location)
        print("""PersonalOS v1.4
------------------------------ MENU ------------------------------
1. Help
2. Local Drive C
3. What's new in the world?
4. Info about patches
5. Calendar
6. PersonalOS mail client
7. User
8. Where am I?
9. Exit
-------------------------------------------------------------------""")
        _choose = input('Enter your choice [1-9]:')
        return _choose

    def print_mail_menu(self,mail_login):
        print('Logged as: ', mail_login)
        print("""PersonalOS mail client v1.0(Alpha)
------------------------------ MENU ------------------------------
1.Send mail
2.Check mail
3.Back
-------------------------------------------------------------------""")
        return input('Enter your choice [1-3]:')

    def print_user_menu(self, username):
        print('Logged as:', username)
        print("""PersonalOS v1.4
------------------------------ USER MENU ------------------------------
1. User info
2. Clear user log
3. Back
-------------------------------------------------------------------""")
        return input('Enter your choice [1-3]:')
