class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def get_details(self):
        return {
            'name': self.name,
            'age': self.age,
            'department': self.department,
            'salary': self.salary
        }


employee_db = {}


def view_employees():
    if not employee_db:
        print("No employees available.")
    else:
        print("\n--- Employee List ---")
        print("{:<10} {:<15} {:<5} {:<12} {:<10}".format('Emp ID', 'Name', 'Age', 'Department', 'Salary'))
        print("-" * 60)
        for emp_id, emp in employee_db.items():
            details = emp.get_details()
            print("{:<10} {:<15} {:<5} {:<12} {:<10}".format(
                emp_id, details['name'], details['age'], details['department'], details['salary']
            ))

def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employee_db:
                print("Employee ID already exists. Please enter a different ID.")
                continue
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            employee_db[emp_id] = Employee(emp_id, name, age, department, salary)
            print("Employee added successfully.")
            break
        except ValueError:
            print("Invalid input. Please enter correct values (e.g., numeric ID, age, and salary).")


def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employee_db:
            emp = employee_db[emp_id]
            details = emp.get_details()
            print("\n--- Employee Found ---")
            print(f"ID        : {emp_id}")
            print(f"Name      : {details['name']}")
            print(f"Age       : {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary    : {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Please enter a valid numeric Employee ID.")


def main_menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee by ID")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()
