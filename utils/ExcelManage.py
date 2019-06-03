import win32com.client as win32
import os

class ExcelConnection():

    def __init__(self, filename, worksheet):
        self.excel = win32.Dispatch('Excel.Application')
        #self.excel.Visible = True
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, filename)
        self.wb = self.excel.Workbooks.Open(filename)
        self.ws = self.wb.Worksheets(worksheet)
    
    def collect(self, row, column):
        #row = 1
        #column = 2
        if row == 0: row = 1
        if column == 0: column = 1
        lis = []
        while (self.ws.Cells(row,column).Value != None ):
            lis.append(str(int(self.ws.Cells(row,column).Value)))
            row = row + 1
        return lis
        
    def close(self):
        self.excel.Quit()


if __name__ == "__main__":
    excel = ExcelConnection('list.xlsx', 'Hoja1')
    print(excel.collect(1,2))
