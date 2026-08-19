# +++++++++++++++++++++++++++++++++++++++++++
#                 Formating old way 
# +++++++++++++++++++++++++++++++++++++++++++
name="osama"
age=22
rank=10
print("my name's : "+ name)
#  number + string erorr 
# print("my name's : "+ name + " and my Age is: " + age )
print("================================================")
#  %s this place holder 
#  print ("My name is : %s "% name)
print ("My name is : %s "% name)
#  this multi varible 
#  print ("my name is %s and my Age is : %d "% (name,age) )
print("================================================")
print ("my name is %s and my Age is : %d "% (name,age) )
print ("my name is %s and my Age is : %d  and my rank is : %d "% (name,age,rank))
"""
(Place holder )
%s -> string 
%d  -> digit
%f  -> floating point .
"""
n="Abdo"
l="python"
y=10
# must in sequance 
print ("my name's : %s & my language : %s & my year %d "%(n,l,y))
# control floating point number 
# %.2f
mynumber=10
print ("My number is %.1f" % mynumber)
# Truncate string 
#%.5f
mylongstr="Hello people of elzero web school i love you All"
print ("message is %.5s !"%mylongstr)