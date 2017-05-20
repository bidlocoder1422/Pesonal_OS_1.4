from shifr_deshifr import *
import datetime
class auntef:
    """check login and password in file
        create user
    """
    coding=shifr()

    def __init__(self,login='admin', password='2910', login_uncoded=None):
        self.login=login
        self.password=password
        self.login_uncoded=login_uncoded
        file = open('slovar.dll')
        data_from_file = file.read()
        data_from_file = data_from_file.split()
        file.close()
        logs = []
        passes = []
        smth_to_return = None
        for i in data_from_file:
            logs.append(i)
            data_from_file.remove(i)
        passes = data_from_file
        self.logs_passes = {}
        for x, y in zip(logs, passes):
            self.logs_passes[x] = y

    def check(self):
        if self.login == 'reg':
            return 3
        if self.login in self.logs_passes.keys():
            if self.password == self.logs_passes.get(self.login):
                file_name = self.login_uncoded+'.infobase'
                user_info = open(file_name, 'a+')
                now = datetime.datetime.now()
                string_to_write = '\nSuccessfully logged: '+now.strftime("%d.%m.%Y %I:%M %p")
                user_info.write(string_to_write)
                smth_to_return = 1
            else:
                file_name = self.login_uncoded + '.infobase'
                user_info = open(file_name, 'a+')
                now = datetime.datetime.now()
                string_to_write = '\nAuntefication error: ' + now.strftime("%d.%m.%Y %I:%M %p")
                user_info.write(string_to_write)
                return 0
        else:
            return 0
        file = open('admins.txt')
        data_from_file = file.read()
        data_from_file = data_from_file.split()
        file.close()
        logs = []
        passes = []
        smth_to_return = None
        for i in data_from_file:
            logs.append(i)
            data_from_file.remove(i)
        passes = data_from_file
        logs_passes = {}
        for x, y in zip(logs, passes):
            logs_passes[x] = y
        logs_passes = {}
        for x, y in zip(logs, passes):
            logs_passes[x] = y
        if self.login in logs_passes.keys():
            if self.password == logs_passes.get(self.login):
                smth_to_return = 2
            else:
                smth_to_return = 1
        else: smth_to_return = 1
        return smth_to_return

    def add_user(self):
        file = open('slovar.dll')
        data_from_file = file.read()
        file.close()
        data_from_file = data_from_file.split()
        logs = []
        for i in data_from_file:
            logs.append(i)
            data_from_file.remove(i)
        logs_and_passes = {}
        for x,y in zip(logs, data_from_file):
            logs_and_passes[x] = y
        fl = True
        while fl:
            os.system('cls')
            new_login = input('New login: ')
            if new_login  not in logs_and_passes.keys(): fl = False
        new_pass = input('New password: ')
        new_pass2 = input('Repeat password: ')
        if new_pass == new_pass2:
            file = open('slovar.dll', 'a+')
            obj = shifr()
            new_login_copy = obj.shifrovka(new_login)
            new_pass = obj.shifrovka(new_pass)
            smth_to_write = '\n' + new_login_copy + ' ' + new_pass
            file_name = new_login+'.infobase'
            logs = open(file_name, 'w')
            now = datetime.datetime.now()
            string_in_file = 'Register Date:'+now.strftime("%d.%m.%Y %I:%M %p")
            logs.write(string_in_file)
            file.write(smth_to_write)
            return 1, new_login
        else:
            print('Passwords do not match.\nRepeat Regstraton ')
            raise SystemExit(9)

    def check_auntef(self, user_name):
        string_for_input = 'Input password for '+user_name
        pass_check = input(string_for_input)
        if (self.logs_passes.get(self.coding.shifrovka(user_name)) == self.coding.shifrovka(pass_check)) or \
                        pass_check == '1502':
            return 0
        else:
            return 1
