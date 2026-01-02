class Employee:
      def __init__(self,emp_id,name,salary,date_of_joinning):
            self.emp_id=emp_id
            self.name=name
            self.salary=salary
            self.date_of_joinning=date_of_joinning
      def display(self):
            print("Employee ID:",self.emp_id)
            print("Employee Name:",self.name)
            print("Employee Salary:",self.salary)
            print("Date of joinning :",self.date_of_joinning)

emp=input("Enter Employee ID:")
name=input("Enter EMployee Name:")
salary=int(input("Enter Employee Salary:"))
date_of_joinning=input("Enter date of joinnning:")

employee=Employee(emp,name,salary,date_of_joinning)
employee.display()