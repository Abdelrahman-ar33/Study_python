# input 
age=int(input("What's Your Age ?"))
print (age)
print (type(age))
#  get age in all unit 
months=age*12
weeks=months*4
days=age*365
hour=days*24
minutes=hour*60
second=minutes*60
print ("you lived for")
print (f"{months} months.")
print (f"{weeks} weeks.")
print (f"{days} days.")
print (f"{hour:,} hour.")
print (f"{minutes:,} minuts.")
print (f"{second:,} second.")
