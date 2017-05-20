from ClassAuntef import *
class commands:
    obj = None

    def user_info(self, username):
        filename = username + '.infobase'
        file = open(filename)
        os.system('cls')
        print('Info about user:', username)
        register_date = file.readline()
        print(register_date)
        print('Last visits: ')
        for line in file:
            if line == register_date:
                pass
            else:
                print(line)
        input('Press Enter to continue')

    def delete_log(self, username):
        input_buf = input('Are you sure? y/n')
        if input_buf == 'n':
            return
        elif input_buf == 'y':
            self.obj = auntef()
            _check = self.obj.check_auntef(username)
            if _check:
                input('Wrong password')
                return
            else:
                filename = username + '.infobase'
                file = open(filename)
                saved_string = file.readline()
                file = open(filename, 'w')
                file.write(saved_string)
                os.system('cls')
                input('Logs was successfully cleared')
    def info_about_last_log(self,user):
        file_name=user+'_info.infobase'
        file=open(file_name)
        data_from_file=file.read()
        print(data_from_file)
        for i in data_from_file:
            pass
