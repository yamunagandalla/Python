class student :
      def __init__(self,student_id,name,marks):
            self.student_id=student_id
            self.name=name
            self.marks=marks
            self.percentage=0
            self.grade=""
      def calculate_percentage(self):
            self.percentage=(self.marks/100)*100
      
            if self.percentage>=90:
                  self.grade="EX"
            elif self.percentage>=80:
                  self.grade="A"
            elif self.percentage>=70:
                  self.grade="B"
            elif self.percentage>=60:
                  self.grade="C"
            elif self.percentage>=50:
                  self.grade="D"
            elif self.percentage>=40:
                  self.grade="E"
            else:
                  self.grade="F"
      def display_details(self):
            print("Student ID:",self.student_id)
            print("Name:",self.name)
            print("Marks:",self.marks)
            print("Percentage:",self.percentage)
            print("Grade:",self.grade)

sid=int(input("Enter Student ID:"))
sname=input("Enter Student Name:")
smarks=int(input("Enter Marks:"))
s=student(sid,sname,smarks)
s.calculate_percentage()
s.display_details()
