import paramiko

PRIVATE_KEY = paramiko.RSAKey.from_private_key_file('C:/path/privatekey.pem')
IP_ADDRESS = 'XXX.XXX.XXX.XXX'
USER = 'username'

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=IP_ADDRESS, username=USER, pkey=PRIVATE_KEY)

stdin, stdout, stderr = ssh_client.exec_command('ls -al')

for stdout_line in stdout.readlines():
    print(stdout_line)

for stderr_line in stderr.readlines():
    print(stderr_line)
