import webbrowser
import xlrd
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
data = xlrd.open_workbook("1.xlsx")
table = data.sheet_by_name(u'Sheet0')

nrows = table.nrows
ncols = table.ncols 
for rowi in range(1):
  rowi = rowi + 10
  test = table.row(rowi)[1].value
  print(rowi)
  print(test)
  time.sleep(10)
  webbrowser.open(test)
