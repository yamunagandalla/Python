class person():
      def __init__(self,name,age):
            self.name=name
            self.age=age
      def display_person(self):
            print("Name:",self.name)
            print("Age:",self.age)

class student(person):
      def __init__(self,name,age,rollno,marks):
            super().__init__(name,age)
            self.rollno=rollno
            self.marks=marks
      def display(self):
            self.display_person()
            print("RollNO:",self.rollno)
            print("Marks:",self.marks)
s1=student("Yamuna",19,36,95)
s1.display()