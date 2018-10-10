from openpyxl import load_workbook
from .Employee import Employee
import os

THIS_FOLDER = os.path.dirname(os.path.relpath(__file__))
report = os.path.join(THIS_FOLDER, 'python-report-1.xlsx')


# Load in the workbook
wb = load_workbook (report, read_only=True)


# Get sheet names
sheets = wb.sheetnames
print(sheets)

ws = wb[sheets[0]]  # get first sheet

print('sheet.max_row ' + str(ws.max_row))
print('sheet.max_column ' + str(ws.max_column))

employeeNumberColumn = 1
startEmployeeNumberRow = 14
full_name_column_index = 2
rate_column_index = 3
position_column_index = 4
calendar_column_index = 6
month_days_count = 31  # TODO get from A1 cell


def init_employee():
    end_employee_table = 0
    employees = []

    for i in range(startEmployeeNumberRow, ws.max_row):
        cell = ws.cell(row=i, column=employeeNumberColumn)
        if cell.value is None:
            end_employee_table += 1
        else:
            end_employee_table = 0
            coordinate = {
                'row': cell.row,
                'column': cell.column
            }
            employee = Employee(coordinate, cell.value)
            employees.append(employee)

        if end_employee_table == 2:
            break

    return employees


def get_employee_full_name(row):
    return ws.cell(row, full_name_column_index).value


def get_employee_rate(row):
    return ws.cell(row, rate_column_index).value


def get_employee_position(row):
    return ws.cell(row, position_column_index).value


def get_employee_timetable(row):
    timetable = {}
    for day in range(0, month_days_count):
        cell = ws.cell(row=row, column=(day + calendar_column_index))
        timetable[(day + 1)] = cell.value

    return timetable


def fill_employees(employees):
    for employee in employees:
        employee_row = employee.coordinate['row']
        employee.full_name = get_employee_full_name(employee_row)
        employee.position = get_employee_position(employee_row)
        employee.rate = get_employee_rate(employee_row)
        employee.timetable = get_employee_timetable(employee_row)


def get_employees():
    employees = init_employee()
    fill_employees(employees)
    return employees

# print(column_index_from_string('A13'))
# for row in ws.rows:
#     for cell in row:
#         if cell.value is not None:
#             print('address:' + cell.coordinate + ' value:' + str(cell.value))
