from openpyxl import load_workbook
from Employee import Employee

# Load in the workbook
wb = load_workbook('./python-report-1.xlsx', read_only=True)

# Get sheet names
sheets = wb.sheetnames
print(sheets)

ws = wb[sheets[0]]  # get first sheet

print('sheet.max_row ' + str(ws.max_row))
print('sheet.max_column ' + str(ws.max_column))

employeeNumberColumn = 1
startEmployeeNumberRow = 14
def init_employee():
    endEmployeeTable = 0
    employees = []

    for i in range(startEmployeeNumberRow, ws.max_row):
        cell = ws.cell(row=i, column=employeeNumberColumn)
        if cell.value is None:
            endEmployeeTable += 1
        else:
            endEmployeeTable = 0
            employee = Employee(cell.coordinate, cell.value)
            employees.append(employee)

        print(i, cell.value)
        print('endEmployeeTable', i, endEmployeeTable)
        if endEmployeeTable == 2:
            break

    return employees


employees = init_employee()
test = 1

# for row in ws.rows:
#     for cell in row:
#         if cell.value is not None:
#             print('address:' + cell.coordinate + ' value:' + str(cell.value))
