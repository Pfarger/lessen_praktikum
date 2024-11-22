class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

        # Сюда добавьте новый атрибут remaining_vacation_days

    def consume_vacation(self, number_out):
        self.remaining_vacation_days -= number_out     
    # print(number_out)
    def get_vacation_details(self):
        return (f'Остаток отпускных дней: {self.remaining_vacation_days}')
    # Сюда добавьте методы consume_vacation и get_vacation_details.


# Пример использования класса:
employee = Employee(first_name="Иван", second_name="Петров", gender="м")
employee.consume_vacation(7)
print(employee.get_vacation_details())
