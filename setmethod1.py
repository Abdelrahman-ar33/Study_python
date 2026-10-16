#  Set methods
#  --------------------------------------------
# clear ()
a={"one","two","three"}
a.clear()
print (a)
print ("==========================")
# union() yani attchad/ same extend or print (b|l) | -> this symbol union 
b={"osama","samir","cool"}
l={1,2,3,4}
# print (b.union(l,p,k,m))
print (b|l)
# add() add item in set add argument 
d={1,2,3,4,5}
d.add(33)
print (d)
print ("==================================")
y={"lolo","koko","samir"}
y.add(9)
f=y.copy()
print (f)
print ("==================================")
g={1,2,3}
# g.remove(7) send error 
g.discard(7) 
#  dont send error 
print (g)
#  pop () send random element from set 
seter={1,2,3,4,8}
print (seter.pop())
# update ()
#  can get list 
j={1,2,3}
k={1,"A","B",2}
j.update(["html","css","ccna"])
j.update(k) 
#  same union 
print (j)