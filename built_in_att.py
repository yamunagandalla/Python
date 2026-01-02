class Student:
      def __init__(self,name,id,marks):
            self.name=name
            self.id=id
            self.marks=marks
s1=Student('yamuna',777,95)
print("class name:",s1.__class__.__name__)
print("Object ID:",id(s1))
print("instance variables :",s1.__dict__)