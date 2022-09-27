import pysftp
import paramiko
# passwords and names for login with sftp
import server_information

sftpHost = server_information.sftpHost
sftpPort = server_information.sftpPort
uname = server_information.uname
passw = server_information.passw
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def send_file(local_path, remote_path):
    with pysftp.Connection(host=sftpHost, username=uname, password=passw, port=sftpPort, cnopts=cnopts) as sftp:
        print('connected')

        sftp.put(local_path, remote_path)

    sftp.close()

