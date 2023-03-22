from dal.table_provider import TableProvider

class TableService():
    def __init__(self):
        self.table_provider = TableProvider()

    def get_table(self):
        return self.table_provider.get_table_from_excel();

    def update_excel(self):
        self.table_provider.update_excel()