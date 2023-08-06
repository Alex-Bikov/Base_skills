class Date:
    def from_string(self, datem: str) -> str:
        data = datem.split('-')
        self.day = data[0]
        self.month = data[1]
        self.year = data[2]
        print(f'День: {self.day}	Месяц: {self.month}	Год: {self.year}')

    def is_date_valid(self, datem: str) -> bool:
        data = datem.split('-')
        if int(data[0]) > 28 and int(date[1]) == 2:
            return False
        elif date[0] > 30 and int(date[1]) not in [1, 3, 5, 7, 8, 10, 12]:
            return False
        else:
            return True

date = Date.from_string('10-12-2077')
print(date)
