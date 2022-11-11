import xlrd
import json

def xls_file_reader(file_path, sheet_name):

    xl_sheet_data = xlrd.open_workbook(file_path)
    ##xl_sheet_data is reference and open_workbook is function to open a file through path
    xl_test_data = xl_sheet_data.sheet_by_name(sheet_name)
    # storing sheet data in xl_sheet_data as providing sheet name in paranthsis
    test_data=dict()
    tc_id, user_name_header, pass_header=xl_test_data.cell_value(0,0), xl_test_data.cell_value(0,1), xl_test_data.cell_value(0,2)
    # tc_id=xl_test_data.cell_value(0,0)first colum zeroth row
    #tc_id=xl_test_data.cell_value(0,1)first colum first row
    # tc_id=xl_test_data.cell_value(0,2)first colum second row
    # user_name_heade=xl_test_data.cell_value(0,0)second colum zeroth row
    # user_name_heade=xl_test_data.cell_value(0,1)second colum first row
    # user_name_head
    #e=xl_test_data.cell_value(0,2)second colum second row
    # pass_header=xl_test_data.cell_value(0,0)
    # pass_header=xl_test_data.cell_value(0,1)
    # pass_header=xl_test_data.cell_value(0,2)

    for j in range(1, xl_test_data.nrows):
        if xl_test_data.cell_value(j,0):
            test_data[xl_test_data.cell_value(j,0)]= {
            user_name_header: xl_test_data.cell_value(j,1),
            pass_header: xl_test_data.cell_value(j,2)
        }
    print(json.dumps(test_data))
    return test_data

# xls_file_reader("C:\\Users\\91766\\PycharmProjects\\AmazonWorkspace\\test\\test_data.xls", "Sheet1")
