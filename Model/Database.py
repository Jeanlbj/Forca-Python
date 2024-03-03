import pyodbc


class Database:
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQL Server};'
                                         'Server=BOOK-SEDCMSP2G4;'
                                         'Database=PalavrasForca;')
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
