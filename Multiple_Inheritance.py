
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)



class Teacher:
    def __init__(self, subject, salary):
        self.subject = subject
        self.salary = salary

    def show_teacher_details(self):
        print("Subject:", self.subject)
        print("Salary:", self.salary)



class TeachingStaff(Person, Teacher):
    def __init__(self, name, age, subject, salary):
      
        Person.__init__(self, name, age)
        Teacher.__init__(self, subject, salary)

    def show_all_details(self):
        self.show_person_details()
        self.show_teacher_details()



t1 = TeachingStaff("Yamuna", 19, "Computer Science", 50000)


t1.show_all_details()
