import ftplib

# Example 1
ftp = ftplib.FTP('ftp.gnu.org')  #Create FTP session and connect to target FTP server; Can specify paramters related to username, password, timeout, encoding, etc.; It is also possible to use the FTP_TLS() method to establish a FTP over TLS connection
ftp.login()  #Use default login credentials - User: anounmous; Password: anonymous@

print(ftp.getwelcome())  #Retrieve and display welcome message sent by the server in reply to the initial connection

files = ftp.dir()  #Return and display directory listing; Typically, the root folder or targetted folder set by admin 

ftp.cwd('/video')  #Change current working directory to the specified path
files = ftp.dir()  #Return and display directory listing
print(ftp.pwd())  #Return and display path of the current directory in order to validate the directory change command from above 


# Example 2
print(ftp.size('fry720.jpg'))  #Return and display the file size in bytes; Note: use relative or absolute paths as required
with open('fry720.jpg', "wb") as download_file:  #Write file in binary mode by selecting a file that is available in the selected directory; Note: use relative or absolute paths as required
    ftp.retrbinary("RETR fry720.jpg", download_file.write)  #Command for downloading the file "RETR filename" and passing the file.write as an object


# Example 3
#with open('fry720.jpg', "rb") as upload_file:  #Read file in binary mode by selecting a file; Note: use relative or absolute paths as required
#    ftp.storbinary("STOR fry720.jpg", upload_file)  # Command for uploading the file "STOR filename" and the file as an object
# This is call results in an error as the required authenication is not provided for uploading/removing/modifying files or directories; only have the capability to read and access files/directories in anonymous mode


# Example 4
ftp.set_pasv(True)  #Explicitly setting the connection to Passive mode; Enabled by default; Set the parameter is False to switch to Active mode


# Example 5
ftp.close()  #Implement command in order to force close connection; Also, it possible to quit() method in order to "politely" close a connection 