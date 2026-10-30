mylist=[1,2,3,4,5,6,7,8,9,10]
print ("============================================")
#  Break
n=10
for number in mylist:
   if number ==6:
    break
   print (number)
print ("============================================")
# continue 
for number in mylist:
   if number ==1:
    continue
   print (number)

#    pass pervent error 
for number in mylist:
 if number==90:
  pass