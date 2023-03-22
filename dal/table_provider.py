import pandas as pd
import os

class TableProvider():
    def __init__(self):
        self.table ="";
        self.path = "C:/Users/URIELY/PycharmProjects/Inbar/data/"

    def get_table_from_excel(self):
        file_path = self.path + os.listdir(self.path)[0]
        self.table  = pd.read_excel(file_path)
        return self.table;

    def update_excel(self):
        file_path = self.path+os.listdir(self.path)[0]
        self.table.to_excel(file_path)


    def update_excel_by_rows(self,data,start_index):
        self.table.to_excel(self.path)