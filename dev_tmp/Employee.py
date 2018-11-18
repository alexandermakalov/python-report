class Employee:
    def __init__(self, coordinate, number):
        self.coordinate = {
            'row': coordinate['row'],
            'column': coordinate['column']
        }
        self.id = number
        self.name = None
        self.rate = None
        self.position = None
