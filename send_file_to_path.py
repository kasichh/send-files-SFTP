import copy_files
import transform_file
import os

# Files:
# local file to upload
file_to_upload = 'CAD_MAT_SUP.csv'

# full path of the local file
local_path = os.getcwd() + r"\ "[0] + file_to_upload

# path to online file
remote_path = "/IMPORTACAO PRODUTOS/CAD_MAT_SUP.csv"


def main_function():
    transform_file.transform_file()
    copy_files.send_file(local_path, remote_path)
    transform_file.delete_file()


if __name__ == '__main__':
    main_function()
