# string indexing & slicing 
#indexing (Access single item )
mystring="i love python"
print (mystring[0]) # index - [0] -> i 
print (mystring[9]) # index - [9] -> t 
# Nagative value  
print (mystring[-1]) # frist character from end index[-1] -> n .
print (mystring[-6]) # frist character from end index[-6] -> p .
print("====================================================\n")
# slicing (Access multiple item ) 
# syntax [start : end] end not include  .
#[start :end:steps].
# mystring1="i love python"
print (mystring[8:11]) # yth 
print (mystring[3:5]) # ov
print (mystring[:10]) # if start is not here will begin from zero 
print (mystring[5:]) # if end  is not here will go to end .
print (mystring[:]) # print full data  .
# Steps 
print (mystring[0::1])
print (mystring[::1])
print(mystring[::2])
print(mystring[::3])
print("====================================================\n")
name="Abdo"
print (name[::2])