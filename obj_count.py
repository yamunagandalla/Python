class Myclass:
      count=0
      def __init__(self):
            Myclass.count+=1
            print("The no.of Objects created:",Myclass.count)
obj1=Myclass()
obj2=Myclass()
obj3=Myclass()