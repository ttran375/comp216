import ftplib

ftp = ftplib.FTP("ftp.gnu.org")
ftp.login()

print(ftp.getwelcome())

# files = ftp.dir()
ftp.cwd("/video")
print(ftp.pwd())

# vid_f = ftp.dir()

print(ftp.size("fry720.jpg"))
