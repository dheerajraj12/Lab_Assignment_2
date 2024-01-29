class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_table(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")

    def display_table(self):
        for employee in self.employees:
            print(employee)


if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sorting_choice = int(input("Enter your choice: "))

    employee_table.sort_table(sorting_choice)

    print("\nSorted Employee Table:")
    employee_table.display_table()
