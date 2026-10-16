# ----------------------------------------------------
# -- set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] item is unique
# --------------------------------------------------------
#  set not orderd not indexed 
myset={1,2,"osama","Ahmed"}
print(myset)
# slicing cant be done 
mytype={1,2,3,"lolo"}
#  error
# print (mytype[0:2])
#  error  Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
#  only tuple 
# mysetone={"osama",100,100.5,True,[1,2,3,4]}
# print (mysetone)
mysetone={"osama",100,100.5,True,(1,2,3,4)}
print (mysetone)
#  item is  unique
mysetwo={1,2,1,3,"osama","osama"}
print(mysetwo)