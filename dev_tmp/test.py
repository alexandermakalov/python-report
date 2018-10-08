from openpyxl import load_workbook

# Load in the workbook
wb = load_workbook('./python-report-1.xlsx', read_only=True)

# Get sheet names
print(wb.sheetnames)

ws = wb['ИЮЛЬ']

for row in ws.rows:
    for cell in row:
        if cell.value is not None:
            print('address:' + cell.coordinate + ' value:' + str(cell.value))
