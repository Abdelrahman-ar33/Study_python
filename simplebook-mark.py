# empty list 
mywebs=[]

#  maximum allow list 
maxium=5
while maxium > 0 :
 web=input("enter the web ? ")
 mywebs.append(f"https://{web.strip().lower()}.com")
 maxium-=1
 print (f"the web site added, {maxium}places left")
else :
 print ("is full")

print ("the sort list :")
if len(mywebs)>0:
 mywebs.sort()

 
index=0 
while index<len(mywebs) :
   print (mywebs[index])
   index+=1