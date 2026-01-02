from datetime import datetime 

a = datetime.now()
b = a.strftime("%Y-%m-%d")
c = a.strftime("%H:%M:%S")
print("Current Date:",b)
print("Current Time:",c)
