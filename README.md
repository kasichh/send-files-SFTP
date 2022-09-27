# Send files using SFTP with python
It's necessary create a file named "server_information.py" with:
## server_information.py:
```
# Virtual machine information 
sftpHost = 'ip.address.to.your.server'
sftpPort = 0000
uname = 'username'
passw = 'password'

# local information
excel_path = r'C:\Users\your\path\to\file.xlsx'
```
##  Run program
To run the full program, run send_file_to_path.py

##  Run program
To run the full program, run send_file_to_path.py

## Run only SFTP sending files
To run only the SFTP file sending, use **copy_files**