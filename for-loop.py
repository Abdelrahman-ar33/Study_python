#  for loop
# for item in iterable_object :
# Do Something With Item
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
#
mynumbers=[1,2,3,4,5,67,8,9]
for numbers in mynumbers :
     if numbers %2==0 : # even or odd
      print (f"is even :{numbers}")
     else :
      
      print(f"is odd :{numbers}")

else:
  print ("loop end")


name="osama"
for names in name :
  print (f"[{names.upper()}]")
  print (name)
