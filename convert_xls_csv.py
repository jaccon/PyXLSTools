import csv
import xlrd
import sys
import os

def ExceltoCSV(excel_file, csv_file_base_path):
    workbook = xlrd.open_workbook(excel_file)
    for sheet_name in workbook.sheet_names():
        print 'processing - ' + sheet_name
        worksheet = workbook.sheet_by_name(sheet_name)
        csv_file_full_path = "./tmp/" + csv_file_base_path + sheet_name.lower().replace(" - ", "_").replace(" ","_") + '.csv'
        csvfile = open(csv_file_full_path, 'wb')
        writetocsv = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for rownum in xrange(worksheet.nrows):
            writetocsv.writerow(
                list(x.encode('utf-8') if type(x) == type(u'') else x for x in worksheet.row_values(rownum)
                )
            )
        csvfile.close()
        print sheet_name + ' has been converted to - ' + csv_file_full_path
if __name__ == '__main__':
    ExceltoCSV(excel_file = sys.argv[1], csv_file_base_path = "data.csv")

os.system('cat ./tmp/*.csv >> exported.csv')

os.system('rm -rf  ./tmp/*.csv')

print "Done !!!! "




