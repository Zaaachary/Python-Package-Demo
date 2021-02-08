import xlrd

def print_xls(filename):
    data = xlrd.open_workbook(filename)
    print("total sheets", data.nsheets)
    for x in range(data.nsheets):
        p = data.sheets()[x].name.encode('utf-8')
        print(p.decode('utf-8'))

    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        ss = table.row_values(i)
        print(ss)
        # for i in range(len(ss)):
        #     print(ss[i])