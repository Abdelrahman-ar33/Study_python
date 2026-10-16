#  setdefault ()
user ={
    "name":"Abdo"
}
print (user)
print (user.setdefault("name","a/n"))
print (user.setdefault("age",55))
print (user)
print ("="*40)
# popitem()
#  get to the last element in dict 
#  old version return random item 
member ={
    "name":"osama",
    "skill":"ps5"
}
#  update element add { }
member.update({"age":22})
print (member.popitem())
print ("="*40)
veiw ={
    "name":"osama",
    "skill":"xbox"
}
# return data in list 
allitem=veiw.items()
#  update .
#  second way 
veiw["age"]=88
print (allitem)
print ("="*40)
#  fromkeys (key,iterable)
# a=('mykeyone','mykeytwo','mykeythree')
# b='X'
# print(dict.fromkeys(a,b))
c=('mykeyone','mykeytwo','mykeythree')
value="l"
print (dict.fromkeys(c,value))