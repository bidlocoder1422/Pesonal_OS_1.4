from ftplib import FTP
ftp = FTP('files.000webhost.com', 'personalossite', '29101998')
filename="vebster.infobase"
file=open(filename, "r")
print(file.read())
try:
    ftp.cwd("vester")
    print("Successfully")
except Exception as e:
    print(e)
