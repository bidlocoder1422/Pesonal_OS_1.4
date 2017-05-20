import os
import smtplib
class gmail:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    def try_to_login(self,login,password):
        self.login=login
        self.password=password
        try:
            self.mail.login(user=self.login, password=self.password)
        except Exception:
            print('If you are sure that login and password are coorect:')
            input('Go to this link and select Turn On\nhttps://www.google.com/settings/security/lesssecureapps')
            return 1
        return 0

    def send_email(self,to,text):
        text += '\n Send from PersonalOS'
        try:
            self.mail.sendmail(self.login, to, text)
            self.mail.close()
            return 0
        except Exception:
            input('Unpredictable error')
            self.mail.close()
            return 1
class mailru:
    pass
    #mail=smtplib.SMTP('',588)
    #mail.ehlo()
    #mail.starttls()
    #def try_to_mailru_login(self,login,password):
    #    pass
