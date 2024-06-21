import ftplib

ftp = ftplib.FTP("ftp.gnu.org")
ftp.login()

print(ftp.getwelcome())

# files = ftp.dir()
ftp.cwd("/video")
print(ftp.pwd())

# vid_f = ftp.dir()

print(ftp.size("fry720.jpg"))

with open("fry720.jpg", "wb") as d_file:
    ftp.retrbinary("RETR fry720.jpg", d_file.write)

with open("fry720.jpg", "wb") as upload_file:
    ftp.storbinary("STOR fry720.jpg", upload_file)

ftp.close()
