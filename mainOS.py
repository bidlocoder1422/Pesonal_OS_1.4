import os
from Menu import *
from FileAccess import *
from News import *
from shifr_deshifr import *
from Calendar_DateTime import *
from commands_dev import *
from current_loc import *
from Mail.mailWork import *
import datetime
def main():
    fl2 = True
    coding = shifr()
    now = datetime.datetime.now()
    print(now.strftime("%d.%m.%Y %I:%M %p"))
    user_name = input('Input Login: ')
    password = input('Input password: ')
    _buf1 = coding.shifrovka(user_name)
    _buf2 = coding.shifrovka(password)
    access = auntef(login=_buf1, password=_buf2, login_uncoded=user_name)
    del _buf2, _buf1
    if user_name == password == 'reg':
       secure_lvl, log = access.add_user()
    else: secure_lvl = access.check()
    if secure_lvl == 0:
        os.system('cls')
        print('Wrong Login or Password')
        input('Try again')
        return
    elif secure_lvl == 1:
        os.system('cls')
        welcome_string = 'Welcome to PersonalOS,'+user_name
        secure = 'user'
        input(welcome_string)
    elif secure_lvl == 2:
        os.system('cls')
        input("Let's code a bit")
        secure = 'dev'
    os.system('cls')
    exit_signal = True
    while(exit_signal):
        menu = Menu(secure)
        key_for_choose = menu.prinmaintmenu(user_name)
        if key_for_choose == '2':
            filework = readfolder(folder='C:/')
            while(filework.fl):
                filework.openfolder()#local Drive
        elif key_for_choose == '3':
            parse = news()
            try:
                parse.print_news()
            except Exception as e:
                print('No connection\nTry later...')
                pass
            input('Press Enter....')#news parser
        elif key_for_choose == '4':
            file_buf = open('PNDEV.infobase')
            data_from_file=file_buf.read()
            os.system('cls')
            input(data_from_file)
        elif key_for_choose == '5':#patch notes
            os.system('cls')
            calendar1 = Date_Work()
            while True:
                year = input('"end" for back to Menu\nInput Year:')
                if year == 'end':
                    break
                fl1 = True
                try:
                    os.system('cls')
                    int(year)
                except Exception:
                    input('Wrong year\nTry again later')
                    fl1 = False
                if fl1:
                    if int(year)<0 or int(year) == 0:
                        print('Wrong year/n')
                    else: calendar1.show_calendar(int(year))#Calendar
        elif key_for_choose == '6':
            _key = 0
            if fl2:
                mail_login = input('Input gmail login: ')
                str_for_input = "Input password for: " + mail_login + ':\n'
                mail_password = input(str_for_input)
                mail = gmail()
                _key = mail.try_to_login(login=mail_login, password=mail_password)
            os.system('cls')
            if not _key:
                fl2 = False
                while True:
                    os.system('cls')
                    _choose = menu.print_mail_menu(mail_login)
                    if _choose == '1':
                        to = input('Input Email: ')
                        text = input('Input text: ')
                        _key = mail.send_email(to,text)
                        if not _key:
                            os.system('cls')
                            str_for_input = 'Message to '+to+' was successfully sent'
                            input(str_for_input)
                    elif _choose == '2':
                        print('Coming in 1.4 or 2.0')
                        input('Thank you for using PersonalOS mail service')
                    elif _choose == '3':
                        os.system('cls')
                        input('Thank you for using PersonalOS mail service')
                        break
                    else:
                        os.system('cls')
                        input('command not found.\n Try again later')
        elif key_for_choose == '7':#mail client
            while True:
                os.system('cls')
                user_info = commands()
                _choose = menu.print_user_menu(user_name)
                if _choose == '1':
                    user_info.user_info(user_name)
                elif _choose == '2':
                    user_info.delete_log(user_name)#User
                elif _choose =='3':
                    break
        elif key_for_choose =='8':#current location
            os.system('cls')
            position=location.return_coord()
        elif key_for_choose == '9':#Exit
            os.system('cls')
            print('PersonalOS v1.4')
            input()
            return
        elif key_for_choose == 'dev':
            pass #ill do it later

if __name__ == '__main__':
    main()
    os.system('pause')
