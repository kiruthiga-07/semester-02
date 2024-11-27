class Employee:
    def __init__(self,emp_id,emp_name,emp_sal,emp_dept):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_sal=emp_sal
        self.emp_dept=emp_dept
    def calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amt=overtime*(self.emp_sal/50)
            total_sal=self.emp_sal+overtime_amt
        else:
            total_sal=self.emp_sal
        return total_sal
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_sal}")
        print(f"Employee Department: {self.emp_dept}")

employees=[
    Employee("Radha","E7876",100000,"Developer"),
    Employee("Shiny","E7499",45000,"Tester"),
    Employee("David","E7900",50000,"Analyst"),
    Employee("Raja","E7698",55000,"Designer")]

for emp in employees:
    emp.print_employee_details()
    print("Salary for 55 Hours: ",emp.calculate_emp_salary(55))
    print()
    
