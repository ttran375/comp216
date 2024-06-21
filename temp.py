import ftplib

ftp = ftplib.FTP("ftp.gnu.org")
ftp.login()

print(ftp.getwelcome())

files = ftp.dir()
