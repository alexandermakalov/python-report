class Employee:
    def __init__(self, coordinate, number):
        self.coordinate = {
            'row': coordinate['row'],
            'column': coordinate['column']
        }
        self.number = number
        self.full_name = None
        self.rate = None
        self.position = None
