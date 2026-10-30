# trypassd=0
# while True :
#  trypassd+=1
#  password=int(input("enter the password ?")) 
#  if password==123 : 
#    print ("correct!")
#    break
#  elif trypassd==5:
#    print (f"account is lock bcause you spend trys {trypassd}")
#    break
print ("===========================================")
tries=4
mainpassword=int (input("enter the password mmmmm?"))
passd=123
while mainpassword != passd  :
 
 tries-=1
 print (f"the tries {tries}")
 mainpassword=int (input("enter the password ?"))
 if tries==0 :
  print (f"the all tries is full {tries}")
  break
else:
 print("password is correct")
