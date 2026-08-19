# +++++++++++++++++++++++++++++++++++++++++++
#                 Formating new way 
# +++++++++++++++++++++++++++++++++++++++++++
name="osama"
age=20
rank=10
#   syntax print("my name is {}".format(varible or text ))
#  place holder {} -> new way 
"""
Place holder 
{:s} string 
{:d} digit 
{:f} floating point 
"""
# print ("my name is {} & my age {}".format(name,age))
# truncate 
print ("my name is {:.2s} & my age {:d} & my rank {:.1f}".format(name,age,rank))
# Format money
#  :_d تنسيق كل ثلاث ارقام 
#  valid format {:_d} ( _ )  ( , )
mymoney=500162976
print("my money in bank is:{:,d} ".format(mymoney))
# Arrange item 
a,b,c="one","two","three"
print("Hello {} {} {}".format(a,b,c))
print("Hello {2} {0} {1}".format(a,b,c)) 
x,y,z=10,20,30
print("Hello {2:.2f} {0:.3f} {1:.1f}".format(x,y,z))
#  format in new version 
myname="Osama"
myage=38
# with out f print ("my name is : {myname} & my age is : {myage}") this 
print(f"my name is : {myname:.2s} & my age is : {myage:.1f}")
