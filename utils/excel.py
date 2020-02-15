#coding: utf-8
import xlrd

class ExcelReadHandle(object):

    def __init__(self, filename, table_index=0):
        wb = xlrd.open_workbook(filename=filename, encoding_override = 'utf-8')
        self.sheet = wb.sheet_by_index(table_index)

    def read_col_num(self):
        return self.sheet.ncols

    def read_row_num(self):
        return self.sheet.nrows

    def read_col(self, col_index):
        return self.sheet.col_values(col_index)

    def read_row(self, row_index):
        return self.sheet.row_values(row_index)

    def read_cell(self, row_index, col_index):
        return self.sheet.cell(row_index, col_index).value

if __name__ == '__main__':
    excel_handler = ExcelReadHandle(u'../../示例表格.xls')
    print excel_handler.read_col_num()