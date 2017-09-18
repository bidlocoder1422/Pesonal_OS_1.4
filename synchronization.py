import sys
from ftplib import FTP
class sync:
    def try_to_connect(self):
        try:
            self.ftp=FTP('files.000webhost.com', 'personalossite', 'pass')
            status="Successfully Connected"
        except Exception as e:
            status="Connetion Error"
        return status
    def sync_files(self, username):
        try:
            self.ftp.cwd(username)
        except Exception as e:
            return -1
