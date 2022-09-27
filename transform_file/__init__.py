import pandas as pd
import openpyxl
import os
from server_information import excel_path
import unidecode

project_path = os.getcwd()
local_path = project_path + r'\CAD_MAT_SUP.csv'


def transform_file():
    # import dataframe
    file = pd.read_excel(excel_path, header=0)

    # transform dataframe columns names
    new_columns = []
    for column in file.columns:
        column = unidecode.unidecode(column)
        column = column.replace(' ', '_')
        column = column.replace(r'/ '[0], '_')
        new_columns.append(column)

    # save new columns names
    file.columns = new_columns

    # save dataframe to csv file
    file.to_csv(local_path, index=False)
    print('extracted file')


def delete_file():
    os.remove(local_path)
    print('file deleted')

if __name__ == '__main__':

    transform_file()

