import xlsxwriter

workbook = xlsxwriter.Workbook("ItemPricesPythonExcel.xlsx")
worksheet = workbook.add_worksheet("firstSheet")


worksheet.write(0,0,"Selling")



workbook.close()

