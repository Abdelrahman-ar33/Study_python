#  clear ()
user ={
    "name":"Osama"
}
user.clear()
print(user)
#  update ()
member ={
    "name":"Osama",
}
member ["age"]=20
#  update (key:value)
member.update({"framework":"react"})
print(member)
# copy ()
main={
    "name":"osama"
}
b=main.copy()
main.update({"rate":10.00})
print(main)
print("="*40)
# print (main.keys())
print(main.values())