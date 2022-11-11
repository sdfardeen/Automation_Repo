import xlrd
import json

def xls_file_reader(file_path, sheet_name):

    xl_sheet_data = xlrd.open_workbook(file_path)
    ##xl_sheet_data is reference and open_workbook is function to open a file through path
    xl_test_data = xl_sheet_data.sheet_by_name(sheet_name)
    # storing sheet data in xl_sheet_data as providing sheet name in paranthsis
    test_data=dict()
    header_list= list()
    #storing header data as list
    for j in range(0,xl_test_data.ncols):
    #kept the cols data in j >> rnge of 0 to ncolumns
        header_list.append(xl_test_data.cell_value(0,j))
        #adding row in header list as a header>>j means colums o,1,2,3...rtc
    print(header_list)


def get_row_data(xl_test_data, header_data, row_index):
    # requirement in paranthesis
    # {"header" : "value"} {"USERNAME"header_Data [1]: "abc" xltestdata.cellvalue(rw_ndex, 1}
    temp_row_data = dict()
    #  allocated one empty to store the rows value as key value type and
    #  finally code will print this to get required dict
    # iterating with headers by pos(index)
    for temp_colum_pos in range(1, len(header_data)):
        # storing in temp_row_data as {"USERNAME":"abc", "PASSWORD":"xyz"}
        # [header_data[temp_colum_pos] -> Username
        # xl_test_data.cell_value(row_index, temp_colum_pos)- > "Abc"
        temp_row_data[header_data[temp_colum_pos]] = xl_test_data.cell_value(row_index, temp_colum_pos)
        print(dict)


    # tc_id, user_name_header, pass_header=xl_test_data.cell_value(0,0), xl_test_data.cell_value(0,1), xl_test_data.cell_value(0,2)

    # for j in range(1, xl_test_data.nrows):
    #     if xl_test_data.cell_value(j,0):
    #         test_data[xl_test_data.cell_value(j,0)]= {
    #         user_name_header: xl_test_data.cell_value(j,1),
    #         pass_header: xl_test_data.cell_value(j,2)
    #     }
    # print(json.dumps(test_data))
    # return test_data

xls_file_reader("C:\\Users\\91766\\PycharmProjects\\AmazonWorkspace\\test\\test_data.xls", "Sheet1")
