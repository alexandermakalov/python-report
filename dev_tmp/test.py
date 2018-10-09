from openpyxl import load_workbook
import os

#The function to work with a relative paths
THIS_FOLDER = os.path.dirname(os.path.relpath(__file__))
grafik = os.path.join(THIS_FOLDER, 'python-report-1.xlsx')

# Load in the workbook
wb = load_workbook (grafik, read_only=True)

# Get sheet names
print(wb.sheetnames)

ws = wb['ИЮЛЬ']

for row in ws.rows:
    for cell in row:
        if cell.value is not None:
            print('address:' + cell.coordinate + ' value:' + str(cell.value))
