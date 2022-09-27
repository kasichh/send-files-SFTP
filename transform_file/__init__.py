import pandas as pd
import openpyxl
import os
from server_information import excel_path

local_path = os.getcwd() + r'\CAD MATERIAIS - SUPORTE.csv'


def transform_file():
    file = pd.read_excel(excel_path)
    file.to_csv(local_path)


def delete_file():
    os.remove(local_path)

if __name__ == '__main__':
    transform_file()
